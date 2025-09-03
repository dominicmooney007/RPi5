#!/usr/bin/env python3
"""
Servo Scanning Pattern
Demonstrates creating scanning patterns with servo
"""

from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_angle=0, max_angle=180)

print("Demonstrating servo scanning patterns...")

# Scan to specific positions
print("Scanning to preset positions")
scan_positions = [0, 45, 90, 135, 180, 135, 90, 45, 0]

for position in scan_positions:
    print(f"Moving to {position} degrees")
    servo.angle = position
    sleep(0.5)

sleep(1)

# Continuous scanning
print("Continuous scanning (3 times)")
for i in range(3):  # Scan 3 times
    print(f"Scan {i+1} of 3")
    
    # Scan right
    for angle in range(0, 181, 10):
        servo.angle = angle
        sleep(0.1)
    
    # Scan left
    for angle in range(180, -1, -10):
        servo.angle = angle
        sleep(0.1)

print("Returning to center")
servo.angle = 90
sleep(1)

print("Detaching servo")
servo.detach()
print("Program complete!")
