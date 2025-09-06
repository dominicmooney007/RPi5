#!/usr/bin/env python3
"""
Smooth Transitions and Effects with PWMOutputDevice
Demonstrates fade effects and smooth frequency changes
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create buzzer
buzzer = PWMOutputDevice(22)

def smooth_frequency_change(start_freq, end_freq, duration=1.0):
    """Smoothly transition between frequencies"""
    print(f"Smooth frequency change: {start_freq}Hz to {end_freq}Hz")
    steps = 50
    buzzer.value = 0.5
    for i in range(steps):
        freq = start_freq + (end_freq - start_freq) * i / steps
        buzzer.frequency = freq
        sleep(duration / steps)
    buzzer.off()

def play_note_smooth(frequency, duration, volume=0.5):
    """Play note with fade in/out to prevent clicks"""
    print(f"Playing {frequency}Hz with smooth fade")
    buzzer.frequency = frequency
    
    # Fade in (50ms)
    fade_steps = 10
    for i in range(fade_steps):
        buzzer.value = volume * i / fade_steps
        sleep(0.005)
    
    # Hold note
    sleep(duration - 0.1)
    
    # Fade out (50ms)
    for i in range(fade_steps, 0, -1):
        buzzer.value = volume * i / fade_steps
        sleep(0.005)
    
    buzzer.off()

def volume_swell(frequency, duration=2.0):
    """Create a volume swell effect"""
    print(f"Volume swell at {frequency}Hz")
    buzzer.frequency = frequency
    steps = 30
    
    # Swell up
    for i in range(steps):
        buzzer.value = i / steps
        sleep(duration / (steps * 2))
    
    # Swell down
    for i in range(steps, 0, -1):
        buzzer.value = i / steps
        sleep(duration / (steps * 2))
    
    buzzer.off()

def tremolo(frequency, duration=2.0, rate=10):
    """Create a tremolo effect (volume modulation)"""
    print(f"Tremolo effect at {frequency}Hz")
    buzzer.frequency = frequency
    cycles = int(duration * rate)
    
    for _ in range(cycles):
        buzzer.value = 0.7
        sleep(1 / (rate * 2))
        buzzer.value = 0.2
        sleep(1 / (rate * 2))
    
    buzzer.off()

def vibrato(center_freq, duration=2.0, depth=50, rate=6):
    """Create a vibrato effect (frequency modulation)"""
    print(f"Vibrato effect around {center_freq}Hz")
    buzzer.value = 0.5
    steps_per_cycle = 20
    cycles = int(duration * rate)
    
    for _ in range(cycles):
        # Frequency oscillation
        for i in range(steps_per_cycle):
            import math
            offset = depth * math.sin(2 * math.pi * i / steps_per_cycle)
            buzzer.frequency = center_freq + offset
            sleep(1 / (rate * steps_per_cycle))
    
    buzzer.off()

def portamento(notes, glide_time=0.1):
    """Play notes with portamento (gliding between pitches)"""
    print("Portamento effect (gliding notes)")
    buzzer.value = 0.5
    
    for i, freq in enumerate(notes):
        if i == 0:
            buzzer.frequency = freq
            sleep(0.3)
        else:
            # Glide from previous frequency to current
            prev_freq = notes[i-1]
            steps = 20
            for step in range(steps):
                glide_freq = prev_freq + (freq - prev_freq) * step / steps
                buzzer.frequency = glide_freq
                sleep(glide_time / steps)
            sleep(0.3)  # Hold the note
    
    buzzer.off()

def doppler_effect(duration=3.0):
    """Simulate Doppler effect (passing sound)"""
    print("Doppler effect (passing sound)")
    base_freq = 500
    buzzer.value = 0.5
    
    # Approaching (frequency increases)
    for i in range(50):
        freq = base_freq * (1 + 0.3 * i / 50)
        volume = 0.1 + 0.4 * i / 50
        buzzer.frequency = freq
        buzzer.value = volume
        sleep(duration / 100)
    
    # Passing (frequency decreases)
    for i in range(50):
        freq = base_freq * (1.3 - 0.3 * i / 50)
        volume = 0.5 - 0.4 * i / 50
        buzzer.frequency = freq
        buzzer.value = volume
        sleep(duration / 100)
    
    buzzer.off()

def echo_effect(frequency, echoes=3):
    """Create an echo effect"""
    print(f"Echo effect at {frequency}Hz")
    
    for i in range(echoes):
        volume = 0.5 * (1 - i / echoes)  # Decreasing volume
        buzzer.frequency = frequency
        buzzer.value = volume
        sleep(0.2)
        buzzer.off()
        sleep(0.1 + i * 0.1)  # Increasing delay

# Demonstration
print("Smooth Transitions and Effects Demonstration")
print("=" * 50)

effects = [
    ("Smooth Frequency Change (200Hz to 800Hz)", 
     lambda: smooth_frequency_change(200, 800, 2)),
    
    ("Smooth Note (440Hz with fade in/out)", 
     lambda: play_note_smooth(440, 1.0)),
    
    ("Volume Swell (523Hz)", 
     lambda: volume_swell(523, 2)),
    
    ("Tremolo Effect (440Hz)", 
     lambda: tremolo(440, 2, rate=8)),
    
    ("Vibrato Effect (440Hz)", 
     lambda: vibrato(440, 2, depth=30, rate=6)),
    
    ("Portamento (Gliding Notes)", 
     lambda: portamento([262, 330, 392, 523, 392, 330, 262])),
    
    ("Doppler Effect (Passing Sound)", 
     lambda: doppler_effect(3)),
    
    ("Echo Effect (600Hz)", 
     lambda: echo_effect(600, echoes=4))
]

for name, effect in effects:
    print(f"\n{name}:")
    effect()
    sleep(1)

print("\n" + "=" * 50)
print("Smooth transitions demonstration complete!")
buzzer.off()
