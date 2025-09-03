#!/usr/bin/env python3
"""
Basic PIR Motion Detection
Demonstrates reading PIR sensor and controlling LED based on motion
"""

from gpiozero import MotionSensor, LED
from time import sleep

# Create sensor and LED objects
pir = MotionSensor(27)
led = LED(17)

print("Waiting for sensor to settle...")
sleep(2)
print("Ready! Looking for motion...")
print("Press Ctrl+C to quit")

# Keep checking for motion
try:
    while True:
        if pir.motion_detected:
            print("Motion detected!")
            led.on()
        else:
            print("No motion")
            led.off()
        
        sleep(0.1)
        
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    led.off()
