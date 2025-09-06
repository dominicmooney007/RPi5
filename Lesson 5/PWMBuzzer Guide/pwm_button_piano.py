#!/usr/bin/env python3
"""
Interactive Button Piano with PWMOutputDevice
Turn buttons into a playable musical instrument
"""

from gpiozero import PWMOutputDevice, Button
from time import sleep

# Setup buzzer
buzzer = PWMOutputDevice(22)

# Create buttons for notes
# Connect buttons to GPIO pins 2, 3, 4, 17, 27
# Adjust GPIO pins based on your wiring
print("Setting up button piano...")
print("Connect buttons to GPIO pins: 2, 3, 4, 17, 27")

try:
    buttons = {
        Button(2): ('C4', 262),
        Button(3): ('D4', 294),
        Button(4): ('E4', 330),
        Button(17): ('F4', 349),
        Button(27): ('G4', 392),
    }
except Exception as e:
    print(f"Error setting up buttons: {e}")
    print("Please check your button connections")
    exit(1)

# Additional scales/modes
scales = {
    'major': {
        Button(2): ('C4', 262),
        Button(3): ('D4', 294),
        Button(4): ('E4', 330),
        Button(17): ('F4', 349),
        Button(27): ('G4', 392),
    },
    'pentatonic': {
        Button(2): ('C4', 262),
        Button(3): ('D4', 294),
        Button(4): ('E4', 330),
        Button(17): ('G4', 392),
        Button(27): ('A4', 440),
    },
    'blues': {
        Button(2): ('C4', 262),
        Button(3): ('Eb4', 311),
        Button(4): ('F4', 349),
        Button(17): ('G4', 392),
        Button(27): ('Bb4', 466),
    }
}

current_scale = 'major'
current_volume = 0.5

def play_button_note(button):
    """Play note while button is pressed"""
    for btn, (note, freq) in buttons.items():
        if btn == button:
            print(f"Playing {note} ({freq} Hz)")
            buzzer.frequency = freq
            buzzer.value = current_volume
            
def stop_note(button):
    """Stop playing when button released"""
    buzzer.off()

def change_volume(delta):
    """Change the volume level"""
    global current_volume
    current_volume = max(0.1, min(1.0, current_volume + delta))
    print(f"Volume: {int(current_volume * 100)}%")

def change_scale(scale_name):
    """Switch to a different scale"""
    global current_scale, buttons
    if scale_name in scales:
        current_scale = scale_name
        buttons = scales[scale_name]
        print(f"Switched to {scale_name} scale")
        demo_scale()

def demo_scale():
    """Play current scale as demonstration"""
    print("Playing scale demo...")
    for button, (note, freq) in buttons.items():
        print(f"  {note}")
        buzzer.frequency = freq
        buzzer.value = current_volume
        sleep(0.3)
        buzzer.off()
        sleep(0.1)

# Assign handlers to all buttons
for button in buttons:
    button.when_pressed = lambda b=button: play_button_note(b)
    button.when_released = lambda b=button: stop_note(b)

# Display instructions
print("\n" + "=" * 50)
print("BUTTON PIANO READY!")
print("=" * 50)
print("\nButton Layout:")
print("  GPIO 2  -> C4")
print("  GPIO 3  -> D4")
print("  GPIO 4  -> E4")
print("  GPIO 17 -> F4")
print("  GPIO 27 -> G4")
print("\nControls:")
print("  Press buttons to play notes")
print("  Press multiple buttons for chords")
print("\nKeyboard Commands:")
print("  'd' - Demo current scale")
print("  '1' - Major scale")
print("  '2' - Pentatonic scale")
print("  '3' - Blues scale")
print("  '+' - Increase volume")
print("  '-' - Decrease volume")
print("  'q' - Quit")
print("-" * 50)

# Demo the scale on startup
demo_scale()

# Main loop for keyboard commands
print("\nPiano is ready! Press buttons to play.")
print("Enter commands or 'q' to quit:")

try:
    while True:
        # Non-blocking check for keyboard input
        try:
            import select
            import sys
            
            # Check if input is available
            if select.select([sys.stdin], [], [], 0.1)[0]:
                cmd = input().lower()
                
                if cmd == 'q':
                    break
                elif cmd == 'd':
                    demo_scale()
                elif cmd == '1':
                    change_scale('major')
                elif cmd == '2':
                    change_scale('pentatonic')
                elif cmd == '3':
                    change_scale('blues')
                elif cmd == '+':
                    change_volume(0.1)
                elif cmd == '-':
                    change_volume(-0.1)
                else:
                    print("Unknown command. Use: d, 1, 2, 3, +, -, q")
        except:
            # Fallback for systems without select
            sleep(0.1)
            
except KeyboardInterrupt:
    print("\n\nPiano stopped by user")

finally:
    print("Shutting down button piano...")
    buzzer.off()
    print("Goodbye!")
