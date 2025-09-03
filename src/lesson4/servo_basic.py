#!/usr/bin/env python3
"""
Basic Servo Control with AngularServo
Demonstrates moving servo to specific angles
"""

from gpiozero import AngularServo
from time import sleep

# Create servo that moves 0-180 degrees
servo = AngularServo(18, min_angle=0, max_angle=180)

print("Demonstrating servo control...")

# Move to specific angles
print("Moving to 0 degrees (minimum)")
servo.angle = 0    # 0 degrees (minimum)
sleep(1)

print("Moving to 90 degrees (center)")
servo.angle = 90   # 90 degrees (center)
sleep(1)

print("Moving to 180 degrees (maximum)")
servo.angle = 180  # 180 degrees (maximum)
sleep(1)

# Move to any angle between 0-180
print("Moving to 45 degrees")
servo.angle = 45   # 45 degrees
sleep(1)

print("Moving to 135 degrees")
servo.angle = 135  # 135 degrees
sleep(1)

# Return to center
print("Returning to center (90 degrees)")
servo.angle = 90
sleep(1)

# Detach servo (stop sending signals)
print("Detaching servo")
servo.detach()
print("Program complete!")
