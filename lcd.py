from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

lcd = CharLCD(compat_mode=True, numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_e=35, pin_rs=37, pins_data=[33, 31, 29, 23])
lcd.write_string(u'Hello\n\rworld!')
smiley = (0b00000, 0b00000, 0b01010, 0b00000, 0b00100, 0b00000, 0b10001, 0b01110)
lcd.create_char(0, smiley)
lcd.write_string(chr(0))
lcd.cursor_mode = 'blink'
time.sleep(100)
lcd.clear()
