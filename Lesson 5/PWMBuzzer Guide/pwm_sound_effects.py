#!/usr/bin/env python3
"""
Sound Effects with PWMOutputDevice
Collection of various sound effects for games and applications
"""

from gpiozero import PWMOutputDevice
from time import sleep
import random

# Create buzzer
buzzer = PWMOutputDevice(22)

def siren(duration=2, min_freq=400, max_freq=800):
    """Create a siren sound effect"""
    print(f"Playing: Siren ({duration} seconds)")
    buzzer.value = 0.5
    steps = 50
    for _ in range(int(duration * 2)):
        # Rising tone
        for i in range(steps):
            buzzer.frequency = min_freq + (max_freq - min_freq) * i / steps
            sleep(0.01)
        # Falling tone
        for i in range(steps):
            buzzer.frequency = max_freq - (max_freq - min_freq) * i / steps
            sleep(0.01)
    buzzer.off()

def laser_sound():
    """Create a laser/shooting sound effect"""
    print("Playing: Laser sound")
    buzzer.value = 0.5
    for freq in range(2000, 100, -50):
        buzzer.frequency = freq
        sleep(0.01)
    buzzer.off()

def explosion():
    """Create an explosion sound effect"""
    print("Playing: Explosion")
    buzzer.value = 1.0
    for _ in range(30):
        buzzer.frequency = random.randint(50, 500)
        sleep(0.02)
        buzzer.value *= 0.9  # Fade out
    buzzer.off()

def phone_ring():
    """Classic phone ring pattern"""
    print("Playing: Phone ring")
    ring_pattern = [
        (1000, 0.1), (0, 0.1), (1000, 0.1), (0, 0.5),
        (1000, 0.1), (0, 0.1), (1000, 0.1), (0, 1.0)
    ]
    for freq, duration in ring_pattern * 2:
        if freq > 0:
            buzzer.frequency = freq
            buzzer.value = 0.5
        else:
            buzzer.off()
        sleep(duration)
    buzzer.off()

def alarm_clock():
    """Increasingly urgent alarm"""
    print("Playing: Alarm clock")
    for intensity in range(1, 4):
        buzzer.value = intensity * 0.3
        for _ in range(intensity * 2):
            buzzer.frequency = 800 * intensity
            sleep(0.1)
            buzzer.off()
            sleep(0.1)
        sleep(0.5)
    buzzer.off()

def ufo_landing():
    """UFO/spaceship landing sound"""
    print("Playing: UFO landing")
    buzzer.value = 0.4
    for freq in range(1500, 100, -10):
        buzzer.frequency = freq
        sleep(0.005)
        if freq % 100 == 0:  # Add wobble effect
            buzzer.frequency = freq + 50
            sleep(0.01)
    buzzer.off()

def sonar_ping():
    """Submarine sonar ping"""
    print("Playing: Sonar ping")
    buzzer.frequency = 1500
    buzzer.value = 0.6
    sleep(0.1)
    buzzer.off()
    sleep(0.05)
    buzzer.frequency = 1200
    buzzer.value = 0.3
    sleep(0.2)
    buzzer.off()

def emergency_alert():
    """Emergency/warning alert sound"""
    print("Playing: Emergency alert")
    for _ in range(3):
        # Two-tone emergency sound
        buzzer.frequency = 800
        buzzer.value = 0.7
        sleep(0.5)
        buzzer.frequency = 600
        sleep(0.5)
    buzzer.off()

# Play all sound effects with delays
print("Sound Effects Demonstration")
print("=" * 30)

effects = [
    ("Siren", lambda: siren(2)),
    ("Laser", laser_sound),
    ("Explosion", explosion),
    ("Phone Ring", phone_ring),
    ("Alarm Clock", alarm_clock),
    ("UFO Landing", ufo_landing),
    ("Sonar Ping", sonar_ping),
    ("Emergency Alert", emergency_alert)
]

for name, effect in effects:
    print(f"\n{name}:")
    effect()
    sleep(1)

print("\nSound effects demonstration complete!")
buzzer.off()
