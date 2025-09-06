#!/usr/bin/env python3
"""
Creating Melodies with PWMOutputDevice
Simple and advanced melody players with example songs
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create buzzer
buzzer = PWMOutputDevice(22)

# Note frequencies
NOTES = {
    'C3': 131, 'D3': 147, 'E3': 165, 'F3': 175, 'G3': 196, 'A3': 220, 'B3': 247,
    'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349, 'G4': 392, 'A4': 440, 'B4': 494,
    'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698, 'G5': 784, 'A5': 880, 'B5': 988,
    'REST': 0
}

def play_melody(notes, tempo=0.5, volume=0.5):
    """
    Play a sequence of notes
    notes: list of (note_name, duration) tuples
    tempo: speed multiplier (smaller = faster)
    volume: 0.0 to 1.0
    """
    for note, duration in notes:
        if note in NOTES:
            freq = NOTES[note]
            if freq > 0:
                buzzer.frequency = freq
                buzzer.value = volume
                sleep(duration * tempo)
                buzzer.off()
            else:
                sleep(duration * tempo)
        sleep(0.05)  # Small gap between notes

def play_advanced_melody(notes):
    """
    Play notes with individual volume control
    notes: list of (note, duration, volume) tuples
    """
    for note, duration, volume in notes:
        if note in NOTES:
            freq = NOTES[note]
            if freq > 0:
                buzzer.frequency = freq
                buzzer.value = volume
                sleep(duration)
                buzzer.off()
            else:
                sleep(duration)
        sleep(0.02)

# Song 1: Mary Had a Little Lamb
print("Playing: Mary Had a Little Lamb")
mary_lamb = [
    ('E4', 0.5), ('D4', 0.5), ('C4', 0.5), ('D4', 0.5),
    ('E4', 0.5), ('E4', 0.5), ('E4', 1.0),
    ('D4', 0.5), ('D4', 0.5), ('D4', 1.0),
    ('E4', 0.5), ('G4', 0.5), ('G4', 1.0),
    ('E4', 0.5), ('D4', 0.5), ('C4', 0.5), ('D4', 0.5),
    ('E4', 0.5), ('E4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('D4', 0.5), ('D4', 0.5), ('E4', 0.5), ('D4', 0.5),
    ('C4', 2.0)
]
play_melody(mary_lamb, tempo=0.4)

sleep(1)

# Song 2: Twinkle Twinkle Little Star
print("\nPlaying: Twinkle Twinkle Little Star")
twinkle = [
    ('C4', 0.5), ('C4', 0.5), ('G4', 0.5), ('G4', 0.5),
    ('A4', 0.5), ('A4', 0.5), ('G4', 1.0),
    ('F4', 0.5), ('F4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('D4', 0.5), ('D4', 0.5), ('C4', 1.0),
    ('G4', 0.5), ('G4', 0.5), ('F4', 0.5), ('F4', 0.5),
    ('E4', 0.5), ('E4', 0.5), ('D4', 1.0),
    ('G4', 0.5), ('G4', 0.5), ('F4', 0.5), ('F4', 0.5),
    ('E4', 0.5), ('E4', 0.5), ('D4', 1.0),
    ('C4', 0.5), ('C4', 0.5), ('G4', 0.5), ('G4', 0.5),
    ('A4', 0.5), ('A4', 0.5), ('G4', 1.0),
    ('F4', 0.5), ('F4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('D4', 0.5), ('D4', 0.5), ('C4', 1.0)
]
play_melody(twinkle, tempo=0.3)

sleep(1)

# Song 3: Happy Birthday (opening)
print("\nPlaying: Happy Birthday (opening)")
birthday = [
    ('C4', 0.5), ('C4', 0.5), ('D4', 1.0), ('C4', 1.0),
    ('F4', 1.0), ('E4', 2.0),
    ('C4', 0.5), ('C4', 0.5), ('D4', 1.0), ('C4', 1.0),
    ('G4', 1.0), ('F4', 2.0)
]
play_melody(birthday, tempo=0.4, volume=0.6)

sleep(1)

# Advanced: Melody with dynamics (varying volume)
print("\nPlaying: Dynamic melody (with volume changes)")
dynamic_melody = [
    ('C4', 0.3, 0.3),  # Quiet start
    ('E4', 0.3, 0.4),  # Getting louder
    ('G4', 0.3, 0.5),  # Medium
    ('C5', 0.5, 0.7),  # Louder
    ('G4', 0.3, 0.5),  # Back to medium
    ('E4', 0.3, 0.4),  # Quieter
    ('C4', 0.5, 0.3),  # Quiet end
]
play_advanced_melody(dynamic_melody)

print("\nMelodies complete!")
buzzer.off()
