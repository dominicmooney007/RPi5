#!/usr/bin/env python3
"""
LED Brightness Control with PWMLED
Demonstrates brightness control and pulsing effects
Note: GPIO18 is a hardware PWM pin on Raspberry Pi 5
"""

from gpiozero import PWMLED
from time import sleep

# Create a PWM LED for brightness control
# Note: GPIO18 is a hardware PWM pin on Raspberry Pi 5
led = PWMLED(18)

print("Demonstrating LED brightness control...")

# Set specific brightness (0 to 1)
print("Setting LED to 50% brightness")
led.brightness = 0.5  # 50% brightness
sleep(2)

# Pulse (fade in and out smoothly)
print("Pulsing LED for 10 seconds...")
led.pulse()
sleep(10)  # Pulse for 10 seconds

# Manual brightness control
print("Gradually increasing brightness from 0% to 100%")
for brightness in range(0, 11):
    led.brightness = brightness / 10  # 0%, 10%, 20%... 100%
    print(f"Brightness: {brightness * 10}%")
    sleep(0.5)

# Turn off
print("Turning LED off")
led.off()
print("Program complete!")
