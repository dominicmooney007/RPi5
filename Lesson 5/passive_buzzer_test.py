#!/usr/bin/env python3
"""
Testing Your Passive Buzzer
Learn how to use a 3-pin passive buzzer module to play different frequencies
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create a PWM device for the passive buzzer
buzzer = PWMOutputDevice(22)

# Musical note frequencies (in Hz)
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523
}

def play_tone(frequency, duration):
    """Play a specific frequency for a duration"""
    if frequency > 0:
        buzzer.frequency = frequency
        buzzer.value = 0.5  # 50% duty cycle
        sleep(duration)
        buzzer.off()
    else:
        sleep(duration)  # Rest

# Test: Play a C major scale
print("Playing C major scale...")
for note_name, freq in notes.items():
    print(f"Playing {note_name} ({freq} Hz)")
    play_tone(freq, 0.5)
    sleep(0.1)  # Small gap between notes

buzzer.off()
print("Test complete!")
