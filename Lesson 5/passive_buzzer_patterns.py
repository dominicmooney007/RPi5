#!/usr/bin/env python3
"""
Quick Musical Patterns with Passive Buzzer
Demonstrates playing melodies and sound effects
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create a PWM device for the passive buzzer
buzzer = PWMOutputDevice(22)

def play_tone(frequency, duration):
    """Play a specific frequency for a duration"""
    if frequency > 0:
        buzzer.frequency = frequency
        buzzer.value = 0.5  # 50% duty cycle
        sleep(duration)
        buzzer.off()
    else:
        sleep(duration)  # Rest

def play_melody(melody, tempo=0.5):
    """Play a list of (frequency, duration) tuples"""
    for freq, duration in melody:
        play_tone(freq, duration * tempo)
        sleep(0.05)  # Tiny gap between notes

# Success sound
success_melody = [
    (262, 0.2),  # C4
    (330, 0.2),  # E4
    (392, 0.2),  # G4
    (523, 0.4),  # C5
]

# Alert sound
alert_melody = [
    (440, 0.1),  # A4
    (0, 0.1),    # Rest
    (440, 0.1),  # A4
    (0, 0.1),    # Rest
    (440, 0.3),  # A4 (longer)
]

print("Playing success sound...")
play_melody(success_melody)

sleep(1)

print("Playing alert sound...")
play_melody(alert_melody)

print("Patterns complete!")
buzzer.off()
