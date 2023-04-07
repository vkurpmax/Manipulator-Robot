from RPLCD.i2c import CharLCD
import time
lcd = CharLCD('PCF8574', 0x27)
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string('Hello World')
lcd.cursor_pos = (1, 0)
lcd.write_string('Welcome')
lcd.cursor_pos = (2, 0)
lcd.write_string('Hi Putu')
lcd.cursor_pos = (3, 1)
lcd.write_string('Thank You')
print('LCD Good to Go')
