#!/usr/bin/env python3
"""
Musical Doorbell System
- Single press: Standard doorbell chime
- Double press: Special melody
- Hold: Continuous tone
"""

from gpiozero import Button, LED, PWMOutputDevice
from time import sleep, time

# Setup components
button = Button(2)
led = LED(17)
buzzer = PWMOutputDevice(22)

# Musical notes
notes = {
    'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349,
    'G4': 392, 'A4': 440, 'B4': 494, 'C5': 523,
    'C3': 131, 'E3': 165, 'G3': 196
}

def play_tone(frequency, duration):
    """Play a tone and flash LED"""
    if frequency > 0:
        buzzer.frequency = frequency
        buzzer.value = 0.5
        led.on()
        sleep(duration)
        buzzer.off()
        led.off()
    else:
        sleep(duration)

def doorbell_chime():
    """Traditional ding-dong sound"""
    print("Ding-dong!")
    play_tone(notes['E4'], 0.3)
    play_tone(notes['C4'], 0.5)

def special_melody():
    """Play a special tune"""
    print("Special melody!")
    melody = [
        ('G4', 0.2), ('E4', 0.2), ('C4', 0.2),
        ('D4', 0.2), ('E4', 0.2), ('G4', 0.4)
    ]
    for note_name, duration in melody:
        play_tone(notes[note_name], duration)
        sleep(0.05)

def alarm_tone():
    """Continuous alarm while button held"""
    print("ALARM! Button held!")
    frequency = 800
    buzzer.frequency = frequency
    buzzer.value = 0.5
    led.blink(on_time=0.1, off_time=0.1)
    
# Button detection variables
last_press_time = 0
press_count = 0

def button_pressed():
    """Handle button press with multi-click detection"""
    global last_press_time, press_count
    
    current_time = time()
    
    # If pressed within 0.5 seconds of last press, it's a multi-click
    if current_time - last_press_time < 0.5:
        press_count += 1
    else:
        press_count = 1
    
    last_press_time = current_time
    
    # Wait a moment to see if more clicks coming
    sleep(0.5)
    
    # Check if button is being held
    if button.is_pressed:
        alarm_tone()
        while button.is_pressed:
            sleep(0.1)
        buzzer.off()
        led.off()
    elif press_count == 1:
        doorbell_chime()
    elif press_count >= 2:
        special_melody()
    
    press_count = 0

# Setup event handler
button.when_pressed = button_pressed

print("Musical Doorbell System Active!")
print("- Single press: Doorbell chime")
print("- Double press: Special melody")
print("- Hold: Alarm tone")
print("Press Ctrl+C to exit")

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("\nDoorbell system deactivated")
    buzzer.off()
    led.off()
