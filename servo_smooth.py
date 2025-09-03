#!/usr/bin/env python3
"""
Smooth Servo Movement
Demonstrates gradual servo movement for smooth motion
"""

from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle=0, max_angle=180)

print("Demonstrating smooth servo movement...")

# Smooth sweep from 0 to 180 degrees
print("Sweeping from 0 to 180 degrees")
for angle in range(0, 181, 5):  # 0 to 180 in steps of 5
    servo.angle = angle
    sleep(0.05)

sleep(0.5)

# Smooth sweep back from 180 to 0
print("Sweeping back from 180 to 0 degrees")
for angle in range(180, -1, -5):  # 180 to 0 in steps of 5
    servo.angle = angle
    sleep(0.05)

sleep(0.5)

# Return to center and detach
print("Returning to center position")
servo.angle = 90
sleep(1)

print("Detaching servo")
servo.detach()
print("Program complete!")
