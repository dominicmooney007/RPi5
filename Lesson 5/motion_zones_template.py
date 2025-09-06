#!/usr/bin/env python3
"""
Template: Motion Detection Zones
A reusable template for creating zone-based responses to motion detection
"""

from gpiozero import MotionSensor, LED, PWMOutputDevice
from time import sleep

# Setup components
pir = MotionSensor(27)
led = LED(17)
buzzer = PWMOutputDevice(22)

# Track motion count
motion_count = 0

def play_tone(frequency, duration):
    """Play a tone"""
    buzzer.frequency = frequency
    buzzer.value = 0.5
    sleep(duration)
    buzzer.off()

def low_alert():
    """Green zone response"""
    print("🟢 GREEN ZONE - Low activity")
    play_tone(262, 0.2)  # C4
    led.on()
    sleep(0.2)
    led.off()

def medium_alert():
    """Yellow zone response"""
    print("🟡 YELLOW ZONE - Moderate activity")
    for _ in range(2):
        play_tone(440, 0.15)  # A4
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)

def high_alert():
    """Red zone response"""
    print("🔴 RED ZONE - High activity!")
    for _ in range(5):
        play_tone(880, 0.1)  # A5
        led.on()
        sleep(0.05)
        led.off()
        sleep(0.05)

def get_zone_response(motion_count):
    """Return appropriate response based on detection count"""
    zones = {
        'green': (0, 2, low_alert),
        'yellow': (3, 5, medium_alert),
        'red': (6, float('inf'), high_alert)
    }
    
    for zone, (min_count, max_count, response) in zones.items():
        if min_count <= motion_count <= max_count:
            print(f"Zone: {zone.upper()}")
            return response
    
    return low_alert  # Default

def handle_motion():
    """Process motion detection"""
    global motion_count
    motion_count += 1
    print(f"Motion detected! Count: {motion_count}")
    
    # Get appropriate response based on zone
    response_function = get_zone_response(motion_count)
    response_function()

# Setup event handler
pir.when_motion = handle_motion

print("=" * 50)
print("MOTION ZONE DETECTION SYSTEM")
print("=" * 50)
print("Green Zone: 1-2 detections (low alert)")
print("Yellow Zone: 3-5 detections (medium alert)")
print("Red Zone: 6+ detections (high alert)")
print("Press Ctrl+C to exit")
print("-" * 50)

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print(f"\nSystem stopped. Total detections: {motion_count}")
    led.off()
    buzzer.off()
