from gpiozero import LED
from time import sleep

# Test each control pin
in1 = LED(23)
in2 = LED(24)
ena = LED(18)

print("Testing IN1...")
in1.on()
sleep(1)
in1.off()

print("Testing IN2...")
in2.on()
sleep(1)
in2.off()

print("Testing ENA...")
ena.on()
sleep(1)
ena.off()

print("All connections tested!")