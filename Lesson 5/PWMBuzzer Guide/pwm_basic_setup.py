#!/usr/bin/env python3
"""
Basic PWMOutputDevice Setup and Usage
Demonstrates fundamental buzzer control with PWM
"""

from gpiozero import PWMOutputDevice
from time import sleep

# Create a PWM buzzer on GPIO pin 22
buzzer = PWMOutputDevice(22)

# Full initialization with all parameters (optional)
# buzzer = PWMOutputDevice(
#     pin=22,           # GPIO pin number
#     active_high=True, # True if buzzer sounds when pin is high
#     initial_value=0,  # Start with buzzer off (0) or on (1)
#     frequency=100     # Initial PWM frequency in Hz
# )

print("Testing basic PWMOutputDevice control...")

# Test 1: Frequency Control
print("\n1. Testing different frequencies:")
frequencies = [262, 440, 880, 1000]  # C4, A4, A5, 1kHz
for freq in frequencies:
    print(f"   Playing {freq} Hz")
    buzzer.frequency = freq
    buzzer.value = 0.5  # 50% duty cycle
    sleep(0.5)
    buzzer.off()
    sleep(0.2)

# Test 2: Volume/Duty Cycle Control
print("\n2. Testing volume levels (440 Hz):")
buzzer.frequency = 440  # A4 note
volumes = [0.1, 0.25, 0.5, 0.75, 1.0]
for vol in volumes:
    print(f"   Volume: {int(vol*100)}%")
    buzzer.value = vol
    sleep(0.5)
    buzzer.off()
    sleep(0.2)

# Test 3: Basic On/Off Control
print("\n3. Testing on/off control:")
buzzer.frequency = 523  # C5
buzzer.value = 0.5
print("   Buzzer ON")
buzzer.on()
sleep(1)
print("   Buzzer OFF")
buzzer.off()

# Check if buzzer is active
print(f"\n4. Buzzer active state: {buzzer.is_active}")

print("\nBasic setup tests complete!")
