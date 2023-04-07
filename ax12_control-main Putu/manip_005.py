from Ax12 import Ax12
from gpiozero import Button
from signal import pause
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time

# - - - - - - - - - - - - - - - - 
# - - - - - - - SETUP - - - - - -
# - - - - - - - - - - - - - - - -
## GPIO SETUP
START = Button(16)          # Using GPIO 16
b = 0

## DYNAMIXEL SETUP
# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = '/dev/ttyUSB0'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

# create AX12 instance with ID 10 
my_dxl_1 = Ax12(1)
my_dxl_2 = Ax12(2)
my_dxl_3 = Ax12(3)
my_dxl_1.set_moving_speed(50)
my_dxl_2.set_moving_speed(50)
my_dxl_3.set_moving_speed(50)

## LCD SETUP
lcd = CharLCD('PCF8574', 0x27)


# - - - - - - - - - - - - - - - - 
# - - - - - - DEFINE  - - - - - -
# - - - - - - - - - - - - - - - -
def SetAngle_4(angle):          
    # Servo_4 Setup
    servo_4 = 12            # Using GPIO 12
    GPIO.setup(servo_4, GPIO.OUT)
    pwm = GPIO.PWM(servo_4, 50)
    pwm.start(0)
    duty = angle / 18 + 2
    GPIO.output(servo_4, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_4, False)
    pwm.ChangeDutyCycle(0)

def SetAngle_5(angle):
    # Servo_5 Setup
    servo_5 = 13            # Using GPIO 13
    GPIO.setup(servo_5, GPIO.OUT)
    pwm = GPIO.PWM(servo_5, 50)
    pwm.start(0)
    duty = angle / 18 + 2
    GPIO.output(servo_5, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_5, False)
    pwm.ChangeDutyCycle(0)

def InputKordinat_X():
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string('INPUT KOORDINAT X,Y,Z')
    lcd.cursor_pos = (1, 0)
    lcd.write_string('KOORDINAT X:')
    lcd.cursor_pos = (3, 0)
    lcd.write_string('TEKAN D JIKA SELESAI')

    
            

# - - - - - - - - - - - - - - - - 
# - - - -  MAIN PROGRAM   - - - -
# - - - - - - - - - - - - - - - -
START.wait_for_press()
print("Pressed")
my_dxl_2.set_goal_position(358)
my_dxl_3.set_goal_position(409)
my_dxl_1.set_goal_position(512)

val1 = int((511.5 - 0) * (180 - 0) / (1023 - 0) + 0)
print("Val-1: %d" % (val1))         # Result: 90 before 74
SetAngle_4(val1)
time.sleep(0.03)
val2 = int((682 - 0) * (180 - 0) / (1023 - 0) + 0)
print("Val-2: %d" % (val2))         # Result: 120 before 0
SetAngle_5(val2)
time.sleep(0.015)
b = 1

START.wait_for_press()
print("Pressed")

InputKordinat_X();
InputKordinat_Y();
InputKordinat_Z();

lcd.setCursor(0,0);
lcd.print("INPUT X= ");
lcd.setCursor(10,0);
lcd.print(X);
lcd.setCursor(0,1);
lcd.print("INPUT Y= ");
lcd.setCursor(10,1);
lcd.print(Y);
lcd.setCursor(0,2);
lcd.print("INPUT Z= ");
lcd.setCursor(10,2);
lcd.print(Z);
lcd.setCursor(0,3);
lcd.print("START=INPUTAN KEDUA");
delay(2000);
Formulasi();

START.wait_for_press()

# - - - - - - - - - - - - - - - - 
# - - - - - DISCONNECT  - - - - -
# - - - - - - - - - - - - - - - -
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()

GPIO.cleanup()