#!/usr/bin/env python3
"""
LED Built-in Methods
Demonstrates using GPIOZero's built-in LED methods
"""

from gpiozero import LED
from time import sleep

led = LED(17)

print("Demonstrating LED built-in methods...")

# Blink continuously (on 1 sec, off 1 sec)
print("Blinking continuously for 10 seconds...")
led.blink()
sleep(10)  # Blink for 10 seconds

# Blink with custom timing
print("Custom blink: 10 times, 0.5 seconds each")
led.blink(on_time=0.5, off_time=0.5, n=10)
sleep(10)  # Wait for blinking to complete

# Toggle the LED state
print("Current LED state will toggle")
led.toggle()  # If off, turns on. If on, turns off.
sleep(2)

print("Turning LED off")
led.off()
print("Program complete!")
