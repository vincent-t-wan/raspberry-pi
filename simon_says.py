import RPi.GPIO as GPIO
import time, sys, random
from threading import Timer

red_out = 22
yellow_out = 24
blue_out = 26
green_out = 32

red_in = 31
yellow_in = 33
blue_in = 35
green_in = 37

# Function for setting up GPIO
def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(red_out, GPIO.OUT)
	GPIO.setup(yellow_out, GPIO.OUT)
	GPIO.setup(blue_out, GPIO.OUT)
	GPIO.setup(green_out, GPIO.OUT)
	GPIO.setup(red_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(yellow_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(blue_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(green_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function that calls when the game is over
def gameover(score):
	print("GAME OVER! Your score is ", score)
	# Clean up GPIO
	GPIO.output(red_out, False)
	GPIO.output(yellow_out, False)
	GPIO.output(blue_out, False)
	GPIO.output(green_out, False)
	GPIO.cleanup()
	exit()

def main():
	if (len(sys.argv) != 2):
		print("Invalid number of arguments. Format: python ./simon_says.py {difficulty (1 = easy, 2 = medium, 3 = hard)})")
		return

	# Set difficulty based on amount of time to guess
	if (sys.argv[1] == '1'):
		time_to_guess = 20
	elif (sys.argv[1] == '2'):
		time_to_guess = 10
	elif (sys.argv[1] == '3'):
		time_to_guess = 5
	else:
		print("Error: Invalid difficulty")
		return

	init()
	# Initially no lights are on
	GPIO.output(red_out, False)
	GPIO.output(yellow_out, False)
	GPIO.output(blue_out, False)
	GPIO.output(green_out, False)

	game = True
	level = 1
	print("For each level, you have", time_to_guess, "seconds to guess. Good luck! Game Starts in:")
	while game:
		# Game runs forever
		print("3")
		time.sleep(1)
		print("2")
		time.sleep(1)
		print("1")
		time.sleep(1)
		print("start!")
		sequence = []
		# Randomly create sequence of lights where the length is based on the level
		for i in range(level):
			sequence.append(random.choice([red_out, yellow_out, blue_out, green_out]))

		# Display sequence of lights
		for output in sequence:
			GPIO.output(output, True)
			time.sleep(0.5)
			GPIO.output(output, False)
			time.sleep(0.5)

		# Start timer for guessing
		timer = Timer(time_to_guess, gameover, args=(level,))
		timer.start()
		guess_phase = True
		guess_sequence = []
		red_pressed = False
		yellow_pressed = False
		blue_pressed = False
		green_pressed = False
		# Every release of a switch appends a guessed color to guess_sequence
		# Repeat until the length of guess_sequence equals the length of sequence
		while (len(guess_sequence) < level):
			if (GPIO.input(red_in) == 1 and not red_pressed):
				red_pressed = True
				time.sleep(0.1)
			elif (GPIO.input(red_in) == 0 and red_pressed):
				guess_sequence.append(red_out)
				red_pressed = False
				time.sleep(0.1)
			elif (GPIO.input(yellow_in) == 1 and not yellow_pressed):
				yellow_pressed = True
				time.sleep(0.1)
			elif (GPIO.input(yellow_in) == 0 and yellow_pressed):
				guess_sequence.append(yellow_out)
				yellow_pressed = False
				time.sleep(0.1)
			elif (GPIO.input(blue_in) == 1 and not blue_pressed):
				blue_pressed = True
				time.sleep(0.1)
			elif (GPIO.input(blue_in) == 0 and blue_pressed):
				guess_sequence.append(blue_out)
				blue_pressed = False
				time.sleep(0.1)
			elif (GPIO.input(green_in) == 1 and not green_pressed):
				green_pressed = True
				time.sleep(0.1)
			elif (GPIO.input(green_in) == 0 and green_pressed):
				guess_sequence.append(green_out)
				green_pressed = False
				time.sleep(0.1)
		timer.cancel()
		# Check if the guessed color sequence matches the actual color sequence
		for i in range(level):
			if (guess_sequence[i] != sequence[i]): break

		# Move on to the next level
		print("Correct!")
		level = level + 1

if __name__ == "__main__":
	try:
		main()
	except:
		GPIO.cleanup()
		pass
