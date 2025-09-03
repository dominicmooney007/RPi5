#!/usr/bin/env python3
"""
PIR Motion Detection with Event Handlers
Demonstrates using event-driven programming for motion detection
"""

from gpiozero import MotionSensor, LED
from time import sleep

pir = MotionSensor(27)
led = LED(17)

# Define what happens when motion is detected
def motion_detected():
    print("Motion detected!")
    led.on()

# Define what happens when motion stops
def no_motion():
    print("Motion stopped")
    led.off()

# Connect the functions to the sensor events
pir.when_motion = motion_detected
pir.when_no_motion = no_motion

print("System armed! Press Ctrl+C to quit")
print("Waiting for motion...")

# Keep the program running
try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    led.off()
