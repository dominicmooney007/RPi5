#!/usr/bin/env python3
"""
Project 2: Interactive Light and Sound
Button-controlled LED and buzzer system
"""

from gpiozero import LED, Button, Buzzer
from time import sleep

# Create components
led = LED(17)
button = Button(2)  # Button on GPIO 2
buzzer = Buzzer(22)

# Define what happens when button is pressed
def button_pressed():
    print("Button pressed!")
    led.on()
    buzzer.on()

# Define what happens when button is released
def button_released():
    print("Button released!")
    led.off()
    buzzer.off()

# Connect functions to button events
button.when_pressed = button_pressed
button.when_released = button_released

print("Interactive Light and Sound System")
print("Press the button to activate LED and buzzer")
print("Release to turn off")
print("Press Ctrl+C to quit")

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("\nProgram stopped")
    led.off()
    buzzer.off()
