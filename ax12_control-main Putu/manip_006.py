from Ax12 import Ax12
from gpiozero import Button
from signal import pause
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time

# Declare Variables
a = 0
b = 0

X = 0.0
Y = 0.0

keypressed = ''

IptKoordinat_X = ''
IptKoordinat_Y = ''

# - - - - - - - - - - - - - - - - 
# - - - - - - - SETUP - - - - - -
# - - - - - - - - - - - - - - - -
## GPIO SETUP
START = Button(16)          # Using GPIO 16

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

## KEYPAD SETUP
# Define the keypad pins
MATRIX = [[1, 2, 3, "A"],
          [4, 5, 6, "B"],
          [7, 8, 9, "C"],
          ["*", 0, "#", "D"]]

ROW = [6, 19, 26, 23]
COL = [17, 27, 22, 5]

# Set the pin mode for the keypad pins
for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to read the keypad
def keypad():
    for j in range(4):
        GPIO.output(COL[j], 0)

        for i in range(4):
            if GPIO.input(ROW[i]) == 0:
                time.sleep(0.02)
                while GPIO.input(ROW[i]) == 0:
                    pass
                return MATRIX[i][j]
            
        GPIO.output(COL[j], 1)
    return None

# Function to iterate keypad()
def key():
    global keypressed
    while True:
        keypressed = keypad()
        if keypressed is not None:
            time.sleep(0.02)
            break

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

def InputKoordinat_X():
    global a, b, X, IptKoordinat_X, keypressed
    count = 0
    while True:
        IptKoordinat_X = ''
        X = 0
        print('LCD Homepage')
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('INPUT KOORDINAT X,Y,Z')
        lcd.cursor_pos = (1, 0)
        lcd.write_string('KOORDINAT X:')
        lcd.cursor_pos = (3, 0)
        lcd.write_string('TEKAN D JIKA SELESAI')
        
        while True:
            key()
            if keypressed == 'D':
                print(keypressed)
                a = 0
                lcd.clear()
                return
            else:
                count += 1
                if keypressed == 'C':
                    print('C2')
                    lcd.clear()
                    lcd.cursor_pos = (1, 0)
                    lcd.write_string('  INPUT BERHASIL ')
                    lcd.cursor_pos = (2, 0)
                    lcd.write_string('   TERHAPUS   ')
                    #InputKoordinat_X = ''
                    a = 0
                    time.sleep(1)
                    break
                elif count >= 0 and count <= 20:
                    lcd.cursor_pos = (2, count)
                    lcd.write_string(str(keypressed))
                    a += 1
                    IptKoordinat_X = f"{IptKoordinat_X}{keypressed}"
                    print(IptKoordinat_X)
                    X = int(IptKoordinat_X)
                    print(X)
                    if keypressed == 'C':
                        print('C1')
                        lcd.clear()
                        lcd.cursor_pos = (1, 0)
                        lcd.write_string('  INPUT BERHASIL ')
                        lcd.cursor_pos = (2, 0)
                        lcd.write_string('   TERHAPUS   ')
                        IptKoordinat_X = ''
                        a = 0
                        time.sleep(1)
                        break
        print('C3')
    print(X)

def InputKoordinat_Y():
    global a, b, Y, IptKoordinat_Y, keypressed
    count = 0
    while True:
        IptKoordinat_Y = ''
        Y = 0
        print('LCD Homepage Y')
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('INPUT KOORDINAT X,Y,Z')
        lcd.cursor_pos = (1, 0)
        lcd.write_string('KOORDINAT Y:')
        lcd.cursor_pos = (3, 0)
        lcd.write_string('TEKAN D JIKA SELESAI')
        
        while True:
            key()
            if keypressed == 'D':
                print(keypressed)
                a = 0
                lcd.clear()
                return
            else:
                count += 1
                if keypressed == 'C':
                    print('C2')
                    lcd.clear()
                    lcd.cursor_pos = (1, 0)
                    lcd.write_string('  INPUT BERHASIL ')
                    lcd.cursor_pos = (2, 0)
                    lcd.write_string('   TERHAPUS   ')
                    #InputKoordinat_Y = ''
                    a = 0
                    time.sleep(1)
                    break
                elif count >= 0 and count <= 20:
                    lcd.cursor_pos = (2, count)
                    lcd.write_string(str(keypressed))
                    a += 1
                    IptKoordinat_Y = f"{IptKoordinat_Y}{keypressed}"
                    print(IptKoordinat_Y)
                    Y = int(IptKoordinat_Y)
                    print(Y)
                    if keypressed == 'C':
                        print('C1')
                        lcd.clear()
                        lcd.cursor_pos = (1, 0)
                        lcd.write_string('  INPUT BERHASIL ')
                        lcd.cursor_pos = (2, 0)
                        lcd.write_string('   TERHAPUS   ')
                        IptKoordinat_Y = ''
                        a = 0
                        time.sleep(1)
                        break
        print('C3')
        print(Y)

# - - - - - - - - - - - - - - - - 
# - - - -  MAIN PROGRAM   - - - -
# - - - - - - - - - - - - - - - -
# SECTION 1: Servo Initial Position
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


# SECTION 2: Input Koordinat X
InputKoordinat_X()

# SECTION 3: Input Koordinat Y
InputKoordinat_Y()

START.wait_for_press()
print('Selesai')

# SECTION 3: Disconnect Servo and Clean GPIO
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()
GPIO.cleanup()