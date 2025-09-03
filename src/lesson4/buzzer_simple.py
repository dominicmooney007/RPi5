#!/usr/bin/env python3
"""
Simple Buzzer Control
Demonstrates basic buzzer operations and beep patterns
"""

from gpiozero import Buzzer
from time import sleep

# Create a buzzer object
buzzer = Buzzer(22)

print("Demonstrating buzzer control...")

# Single beep
print("Single beep (0.5 seconds)")
buzzer.on()
sleep(0.5)  # Beep for 0.5 seconds
buzzer.off()
sleep(1)

# Multiple beeps
print("Three short beeps")
for i in range(3):
    buzzer.on()
    sleep(0.1)  # Short beep
    buzzer.off()
    sleep(0.1)  # Short pause

sleep(1)

# Using built-in beep method
print("Continuous beeping for 5 seconds")
buzzer.beep()  # Continuous beeping
sleep(5)
buzzer.off()

sleep(1)

# Custom beep pattern
print("Custom pattern: 10 quick beeps")
buzzer.beep(on_time=0.1, off_time=0.1, n=10)  # 10 quick beeps
sleep(3)

print("Program complete!")
