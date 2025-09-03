#!/usr/bin/env python3
"""
Musical Tones with TonalBuzzer
Demonstrates playing musical notes and melodies
"""

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

# Create a tonal buzzer (for musical notes)
buzzer = TonalBuzzer(22)

print("Demonstrating musical tones...")

# Play a single tone
print("Playing A4 note for 1 second")
buzzer.play(Tone("A4"))  # Play A4 note
sleep(1)
buzzer.stop()
sleep(0.5)

# Play a simple melody
print("Playing a scale: C4 to C5")
notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

for note in notes:
    print(f"Playing {note}")
    buzzer.play(Tone(note))
    sleep(0.5)
    buzzer.stop()
    sleep(0.1)

sleep(1)

# Play with frequency directly
print("Playing 440 Hz (A4 note) directly")
buzzer.play(440)  # 440 Hz (A4 note)
sleep(1)
buzzer.stop()

print("Program complete!")
