#!/usr/bin/env python3
"""
Basic LED Control
Demonstrates turning an LED on/off and blinking
Uses a 3-pin LED module with built-in resistor
"""

from gpiozero import LED
from time import sleep

# Create an LED object on GPIO 17
led = LED(17)

# Turn LED on and off
print("Turning LED on...")
led.on()
sleep(1)    # Wait 1 second

print("Turning LED off...")
led.off()
sleep(1)

# Blink the LED 5 times
print("Blinking LED 5 times...")
for i in range(5):
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

print("Program complete!")
