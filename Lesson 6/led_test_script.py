from gpiozero import LED
from time import sleep

# LED module connected to GPIO 17
led = LED(17)

print("Testing LED module...")
for _ in range(3):
    led.on()
    print("LED ON")
    sleep(1)
    led.off()
    print("LED OFF")
    sleep(1)
print("Test complete!")