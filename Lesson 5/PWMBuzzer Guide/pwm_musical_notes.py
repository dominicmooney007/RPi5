#!/usr/bin/env python3
"""
Playing Musical Notes with PWMOutputDevice
Complete note frequency reference and playback functions
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create buzzer
buzzer = PWMOutputDevice(22)

# Dictionary of musical note frequencies (3rd, 4th and 5th octave)
NOTES = {
    # 3rd Octave
    'C3': 131, 'C#3': 139, 'D3': 147, 'D#3': 156,
    'E3': 165, 'F3': 175, 'F#3': 185, 'G3': 196,
    'G#3': 208, 'A3': 220, 'A#3': 233, 'B3': 247,
    
    # 4th Octave (Middle)
    'C4': 262, 'C#4': 277, 'D4': 294, 'D#4': 311,
    'E4': 330, 'F4': 349, 'F#4': 370, 'G4': 392,
    'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 494,
    
    # 5th Octave
    'C5': 523, 'C#5': 554, 'D5': 587, 'D#5': 622,
    'E5': 659, 'F5': 698, 'F#5': 740, 'G5': 784,
    'G#5': 831, 'A5': 880, 'A#5': 932, 'B5': 988,
    
    # Special
    'REST': 0  # Silence
}

def play_note(note_name, duration=0.5, volume=0.5):
    """Play a single musical note"""
    if note_name in NOTES:
        frequency = NOTES[note_name]
        if frequency > 0:
            buzzer.frequency = frequency
            buzzer.value = volume
            sleep(duration)
            buzzer.off()
        else:
            sleep(duration)  # Rest
    else:
        print(f"Note {note_name} not found")

# Test: Play chromatic scale
print("Playing chromatic scale (C4 to C5):")
chromatic = ['C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 
             'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 'C5']

for note in chromatic:
    print(f"  Playing {note} ({NOTES[note]} Hz)")
    play_note(note, 0.3)
    sleep(0.1)

sleep(1)

# Test: Play C major scale
print("\nPlaying C major scale:")
c_major = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

for note in c_major:
    print(f"  Playing {note}")
    play_note(note, 0.5)

sleep(1)

# Test: Different volumes
print("\nPlaying A4 at different volumes:")
volumes = [0.2, 0.4, 0.6, 0.8, 1.0]
for vol in volumes:
    print(f"  Volume: {int(vol*100)}%")
    play_note('A4', 0.5, vol)
    sleep(0.2)

print("\nMusical notes test complete!")
buzzer.off()
