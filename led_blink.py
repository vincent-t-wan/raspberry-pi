#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
# loop through 50 times, on/off for 1 second
for i in range(50):
    GPIO.output(40,False)
    GPIO.output(7,True)
    time.sleep(1)
    GPIO.output(7,False)
    GPIO.output(40,True)
    time.sleep(1)
GPIO.cleanup()
