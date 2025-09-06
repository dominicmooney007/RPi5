#!/usr/bin/env python3
"""
Smart Alarm System with Zones
- Motion detection triggers different responses based on armed state
- Servo acts as security camera
- Musical alerts for different events
"""

from gpiozero import MotionSensor, LED, Button, PWMOutputDevice, AngularServo
from time import sleep
from datetime import datetime

# Component setup
pir = MotionSensor(27)
alarm_led = LED(17)      # Red LED for alarm
status_led = LED(23)      # Green LED for system status
buzzer = PWMOutputDevice(22)
servo = AngularServo(18, min_angle=0, max_angle=180)
arm_button = Button(2)

# System states
class SecuritySystem:
    def __init__(self):
        self.armed = False
        self.alert_level = 0  # 0=off, 1=low, 2=medium, 3=high
        self.motion_count = 0
        self.last_position = 90
        
system = SecuritySystem()

# Musical tones for different alerts
def play_tone(frequency, duration):
    """Play a single tone"""
    buzzer.frequency = frequency
    buzzer.value = 0.5
    sleep(duration)
    buzzer.off()

def system_armed_sound():
    """Play arming confirmation sound"""
    print("🔒 System ARMED")
    for freq in [523, 659, 784]:  # C5, E5, G5
        play_tone(freq, 0.1)
        status_led.on()
        sleep(0.05)
        status_led.off()
    status_led.on()

def system_disarmed_sound():
    """Play disarming confirmation sound"""
    print("🔓 System DISARMED")
    for freq in [784, 659, 523]:  # G5, E5, C5
        play_tone(freq, 0.1)
        alarm_led.on()
        sleep(0.05)
        alarm_led.off()
    status_led.off()

def low_alert():
    """Low priority alert - single beep"""
    print("📢 Low alert - motion detected")
    play_tone(440, 0.2)  # A4
    alarm_led.on()
    sleep(0.2)
    alarm_led.off()

def medium_alert():
    """Medium priority alert - double beep"""
    print("⚠️  Medium alert - repeated motion!")
    for _ in range(2):
        play_tone(880, 0.15)  # A5
        alarm_led.on()
        sleep(0.1)
        alarm_led.off()
        sleep(0.1)

def high_alert():
    """High priority alert - alarm sequence"""
    print("🚨 HIGH ALERT - INTRUDER DETECTED!")
    for _ in range(5):
        # Alternating high-low tones
        play_tone(988, 0.1)  # B5
        alarm_led.on()
        sleep(0.05)
        play_tone(659, 0.1)  # E5
        alarm_led.off()
        sleep(0.05)

def scan_area():
    """Servo scans the area and returns to motion direction"""
    angles = [45, 90, 135, 90]
    for angle in angles:
        servo.angle = angle
        sleep(0.3)
    return 90  # Return center position

def track_motion():
    """Simulate camera tracking to motion source"""
    global system
    
    # Simulate directional tracking
    if system.last_position <= 90:
        new_position = system.last_position + 30
    else:
        new_position = system.last_position - 30
    
    # Constrain to valid range
    new_position = max(0, min(180, new_position))
    
    print(f"📹 Camera tracking to {new_position}°")
    servo.angle = new_position
    system.last_position = new_position

def handle_motion():
    """Process motion detection based on system state"""
    if not system.armed:
        print("Motion detected (system not armed)")
        return
    
    system.motion_count += 1
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Motion #{system.motion_count}")
    
    # Track with camera
    track_motion()
    
    # Escalate alert level based on motion count
    if system.motion_count <= 2:
        system.alert_level = 1
        low_alert()
    elif system.motion_count <= 5:
        system.alert_level = 2
        medium_alert()
    else:
        system.alert_level = 3
        high_alert()
        scan_area()  # Full area scan on high alert

def toggle_armed_state():
    """Toggle system armed/disarmed state"""
    system.armed = not system.armed
    system.motion_count = 0
    system.alert_level = 0
    
    if system.armed:
        system_armed_sound()
        servo.angle = 90  # Center position
    else:
        system_disarmed_sound()
        servo.detach()  # Save power when disarmed

# Event handlers
pir.when_motion = handle_motion
arm_button.when_pressed = toggle_armed_state

# Initialize system
print("=" * 50)
print("SMART ALARM SYSTEM WITH ZONES")
print("=" * 50)
print("Press button to ARM/DISARM system")
print("Motion detection triggers escalating alerts")
print("Servo camera tracks motion source")
print("Press Ctrl+C to exit")
print("-" * 50)

servo.angle = 90  # Start at center
status_led.off()  # Start disarmed

try:
    while True:
        # Blink status LED when armed
        if system.armed and system.alert_level == 0:
            status_led.on()
            sleep(0.5)
            status_led.off()
            sleep(0.5)
        else:
            sleep(1)
            
except KeyboardInterrupt:
    print("\n" + "=" * 50)
    print("System shutdown")
    print(f"Total detections: {system.motion_count}")
    print("=" * 50)
    servo.detach()
    alarm_led.off()
    status_led.off()
    buzzer.off()
