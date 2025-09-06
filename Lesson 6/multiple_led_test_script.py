from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

# Test each LED
for i, led in enumerate([led1, led2, led3]):
    print(f"Testing LED {i+1}")
    led.on()
    sleep(1)
    led.off()
    sleep(0.5)