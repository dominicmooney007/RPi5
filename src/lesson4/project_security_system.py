#!/usr/bin/env python3
"""
Complete Smart Security System
Advanced project combining all components with logging and reset functionality
"""

from gpiozero import MotionSensor, LED, Buzzer, AngularServo, Button
from time import sleep
from datetime import datetime

# Setup all components
pir = MotionSensor(27)
alarm_led = LED(17)
status_led = LED(23)
buzzer = Buzzer(22)
servo = AngularServo(18, min_angle=0, max_angle=180)
reset_button = Button(2)

# System variables
motion_count = 0
system_armed = True

def scan_area():
    """Servo scans the area"""
    for angle in [0, 45, 90, 135, 180, 135, 90, 45, 0]:
        servo.angle = angle
        sleep(0.3)

def motion_detected():
    """Handle motion detection"""
    global motion_count
    if system_armed:
        motion_count += 1
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] Motion #{motion_count} detected!")
        
        # Quick alarm
        alarm_led.blink(on_time=0.1, off_time=0.1, n=10)
        buzzer.beep(on_time=0.1, off_time=0.1, n=5)
        
        # Scan with servo
        scan_area()

def reset_system():
    """Reset the system"""
    global motion_count, system_armed
    print("System reset!")
    motion_count = 0
    system_armed = True
    status_led.on()
    buzzer.beep(on_time=0.5, off_time=0, n=1)

# Connect functions to events
pir.when_motion = motion_detected
reset_button.when_pressed = reset_system

# Initialize system
print("Smart Security System Starting...")
print("-" * 40)
servo.angle = 90  # Center position
status_led.on()   # System armed indicator
sleep(2)          # Let PIR settle
print("System Armed!")
print("- Motion detection active")
print("- Press reset button to reset counter")
print("- Press Ctrl+C to shutdown")
print("-" * 40)

try:
    while True:
        # Status indicator
        if system_armed:
            status_led.on()
        else:
            status_led.blink()
        
        sleep(1)
        
except KeyboardInterrupt:
    print("\n" + "-" * 40)
    print(f"System shutting down")
    print(f"Total detections: {motion_count}")
    print("-" * 40)
    servo.detach()
    alarm_led.off()
    status_led.off()
    buzzer.off()
