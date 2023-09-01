import RPi.GPIO as GPIO
import signal

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.OUT)

def stop_signals_handler(signum, frame):
	GPIO.output(36, False)
	GPIO.output(40, False)
	GPIO.cleanup()
signal.signal(signal.SIGINT, stop_signals_handler)
signal.signal(signal.SIGTERM, stop_signals_handler)

try:
	while True:
		if GPIO.input(38) == 0:
			GPIO.output(36, True)
			GPIO.output(40, False)
		else:
			GPIO.output(36, False)
			GPIO.output(40, True)
finally:
	GPIO.output(36, False)
	GPIO.output(40, False)
	GPIO.cleanup()
