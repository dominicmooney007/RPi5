#!/usr/bin/env python3
"""
Morse Code Generator with PWMOutputDevice
Convert text messages to Morse code audio signals
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create buzzer
buzzer = PWMOutputDevice(22)

def morse_code(message, wpm=20):
    """
    Convert text to Morse code sounds
    wpm: Words per minute (affects speed)
    """
    # Timing based on words per minute
    dot_length = 1.2 / wpm
    
    # Morse code dictionary
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..',
        "'": '.----.', '!': '-.-.--', '/': '-..-.',
        '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
    }
    
    buzzer.frequency = 600  # Standard Morse tone
    
    print(f"Transmitting: '{message}' at {wpm} WPM")
    print("Morse: ", end="")
    
    for char in message.upper():
        if char in morse:
            print(morse[char], end=" ")
            for symbol in morse[char]:
                if symbol == '.':
                    # Dot (dit)
                    buzzer.value = 0.5
                    sleep(dot_length)
                    buzzer.off()
                elif symbol == '-':
                    # Dash (dah)
                    buzzer.value = 0.5
                    sleep(dot_length * 3)
                    buzzer.off()
                else:  # Space between words
                    sleep(dot_length * 7)
                sleep(dot_length)  # Gap between dots/dashes
            sleep(dot_length * 3)  # Gap between letters
        else:
            print(f"[{char}?]", end=" ")
    
    buzzer.off()
    print("\nTransmission complete!")

# Demonstration
print("Morse Code Generator")
print("=" * 40)

# Test 1: SOS (emergency signal)
print("\n1. Emergency Signal:")
morse_code("SOS", wpm=15)
sleep(2)

# Test 2: Hello World
print("\n2. Greeting:")
morse_code("HELLO WORLD", wpm=20)
sleep(2)

# Test 3: Numbers
print("\n3. Numbers:")
morse_code("123 456 789", wpm=18)
sleep(2)

# Test 4: Mixed message
print("\n4. Mixed message:")
morse_code("TESTING 123 ABC", wpm=22)
sleep(2)

# Interactive mode
print("\n" + "=" * 40)
print("Interactive Morse Code Mode")
print("Enter text to convert to Morse code")
print("Type 'quit' to exit")
print("-" * 40)

while True:
    try:
        text = input("\nEnter message: ")
        if text.lower() == 'quit':
            break
        if text:
            speed = input("Enter WPM (default 20): ")
            wpm = int(speed) if speed else 20
            morse_code(text, wpm)
    except KeyboardInterrupt:
        break
    except ValueError:
        print("Invalid WPM, using default (20)")
        morse_code(text, 20)

print("\nMorse code generator stopped")
buzzer.off()
