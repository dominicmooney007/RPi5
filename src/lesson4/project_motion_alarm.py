#!/usr/bin/env python3
"""
Project 1: Motion-Activated Alarm
Combines PIR sensor, LED, buzzer, and servo for an alarm system
"""

from gpiozero import MotionSensor, LED, Buzzer, AngularServo
from time import sleep

# Create all component objects
pir = MotionSensor(27)
led = LED(17)
buzzer = Buzzer(22)
servo = AngularServo(18, min_angle=0, max_angle=180)

def trigger_alarm():
    """Activate all alarm components"""
    print("ALARM! Motion detected!")
    
    # Flash LED and buzzer 5 times
    print("Activating alarm sequence...")
    for i in range(5):
        led.on()
        buzzer.on()
        sleep(0.2)
        led.off()
        buzzer.off()
        sleep(0.2)
    
    # Move servo to alert positions
    print("Servo scanning...")
    servo.angle = 180  # Full right
    sleep(1)
    servo.angle = 0    # Full left
    sleep(1)
    servo.angle = 90   # Return to center
    sleep(0.5)

# Set up motion detection
pir.when_motion = trigger_alarm

print("Security system armed!")
print("Waiting for motion...")
print("Press Ctrl+C to quit")

# Initialize servo position
servo.angle = 90

try:
    # Keep program running
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("\nSystem disarmed")
    servo.detach()
    led.off()
    buzzer.off()
