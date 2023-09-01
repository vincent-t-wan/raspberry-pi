import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

servo = GPIO.PWM(40, 50)
servo.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            servo.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            servo.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
servo.stop()
GPIO.cleanup()
