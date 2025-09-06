#!/usr/bin/env python3
"""
Template: Play Any Melody
A reusable template for creating and playing songs with passive buzzer
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create buzzer
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

def create_song(song_notes, tempo=0.4):
    """
    Play a song from note names
    song_notes: list of (note_name, duration) tuples
    """
    note_freq = {
        'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349,
        'G4': 392, 'A4': 440, 'B4': 494, 'C5': 523,
        'REST': 0
    }
    
    for note, duration in song_notes:
        if note in note_freq:
            play_tone(note_freq[note], duration * tempo)
            sleep(0.05)

# Example: "Happy Birthday" opening
print("Playing 'Happy Birthday' opening...")
birthday = [
    ('C4', 0.5), ('C4', 0.5), ('D4', 1), ('C4', 1),
    ('F4', 1), ('E4', 2)
]
create_song(birthday)

sleep(1)

# Example: "Twinkle Twinkle Little Star" opening
print("Playing 'Twinkle Twinkle' opening...")
twinkle = [
    ('C4', 0.5), ('C4', 0.5), ('G4', 0.5), ('G4', 0.5),
    ('A4', 0.5), ('A4', 0.5), ('G4', 1),
    ('F4', 0.5), ('F4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('D4', 0.5), ('D4', 0.5), ('C4', 1)
]
create_song(twinkle, tempo=0.3)

print("Songs complete!")
buzzer.off()
