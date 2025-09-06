from gpiozero import Motor, PWMOutputDevice
from time import sleep

pwm = PWMOutputDevice(18)
motor = Motor(23, 24)

# Test different speeds
for speed in [0.3, 0.5, 0.7, 1.0]:
    print(f"Testing {int(speed*100)}% speed")
    pwm.value = speed
    motor.forward()
    sleep(2)

motor.stop()
pwm.close()
motor.close()