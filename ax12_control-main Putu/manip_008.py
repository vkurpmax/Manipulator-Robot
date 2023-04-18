from Ax12 import Ax12
from gpiozero import Button
from signal import pause
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
import math

# Declare Variables
a = 0
b = 0

X = 0.0
Y = 0.0
Z = 0.0

L1 = 0      # 2147483666
L2 = 0
L3 = 0

h = 0.0
theta1 = 0.0
c3 = 0.0
s3 = 0.0
s3a = 0.0
theta3 = 0.0
p1 = 0.0
p2 = 0.0
theta2a = 0.0
theta2 = 0.0

T1a = 0.0
T2a = 0.0
T3a = 0.0

T1 = 0.0
T2 = 0.0
T3 = 0.0

keypressed = ''

IptKoordinat_X = ''
IptKoordinat_Y = ''
IptKoordinat_Z = ''

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
        print('LCD Homepage X')
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
                    a = 0
                    time.sleep(1)
                    break
                elif count >= 0 and count <= 20:
                    lcd.cursor_pos = (2, count)
                    lcd.write_string(str(keypressed))
                    a += 1
                    IptKoordinat_X = f"{IptKoordinat_X}{keypressed}"
                    X = int(IptKoordinat_X)
                    print(X)
                    if keypressed == 'C':
                        print('C1')
                        lcd.clear()
                        lcd.cursor_pos = (1, 0)
                        lcd.write_string('  INPUT BERHASIL ')
                        lcd.cursor_pos = (2, 0)
                        lcd.write_string('   TERHAPUS   ')
                        a = 0
                        time.sleep(1)
                        break
        print('C3')

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
                        a = 0
                        time.sleep(1)
                        break
        print('C3')
        print(Y)

def InputKoordinat_Z():
    global a, b, Z, IptKoordinat_Z, keypressed
    count = 0
    while True:
        IptKoordinat_Z = ''
        Z = 0
        print('LCD Homepage Z')
        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string('INPUT KOORDINAT X,Y,Z')
        lcd.cursor_pos = (1, 0)
        lcd.write_string('KOORDINAT Z:')
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
                    a = 0
                    time.sleep(1)
                    break
                elif count >= 0 and count <= 20:
                    lcd.cursor_pos = (2, count)
                    lcd.write_string(str(keypressed))
                    a += 1
                    IptKoordinat_Z = f"{IptKoordinat_Z}{keypressed}"
                    print(IptKoordinat_Z)
                    Z = int(IptKoordinat_Z)
                    print(Z)
                    if keypressed == 'C':
                        print('C1')
                        lcd.clear()
                        lcd.cursor_pos = (1, 0)
                        lcd.write_string('  INPUT BERHASIL ')
                        lcd.cursor_pos = (2, 0)
                        lcd.write_string('   TERHAPUS   ')
                        a = 0
                        time.sleep(1)
                        break
        print('C3')
        print(Z)

def Formulasi():
    global L1, L2, L3
    global h, Z
    global X, Y, theta1
    global c3, s3, s3a, theta3
    global p1, p2, theta2a, theta2
    global T1a, T2a, T3a
    global T1, T2, T3

    L1 = 85     # mm
    L2 = 165    # mm
    L3 = 155    # mm

    # Formulasi Invers Kinematics Robot Manipulator
    h = Z - L1  # mm    # Is h = height?
    theta1 = math.atan2(Y, X)    # radian

    c3 = (X*X + Y*Y + h*h - L2*L2 - L3*L3) / (2*L2*L3)  # dunno what is c3?
    s3 = -math.sqrt(1 - c3*c3)  # for down elbow
    s3a = math.sqrt(1 - c3*c3)  # for up elbow
    theta3 = math.atan2(s3, c3) # radian
    p1 = (Y*L3*math.cos(theta3)+Y*L2) + (X*L3*math.sin(theta3))
    p2 = (X*L3*math.cos(theta3)+X*L2) - (Y*L3*math.sin(theta3))
    theta2a = math.atan2(p1, p2)    # radian
    theta2 = 2*theta2a  # radian

    T1a = theta1 * 180.0 / math.pi  # degree
    T2a = theta2 * 180.0 / math.pi  # degree
    T3a = theta3 * 180.0 / math.pi  # degree

    T1 = (150 + T1a) * 3.41
    T2 = (60 + T2a) * 3.41
    T3 = (150 + T3a) * 3.41


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
print(X)
print("Ipt Koordinat X: %s" % (IptKoordinat_X))

# SECTION 3: Input Koordinat Y
InputKoordinat_Y()
print(Y)
print("Ipt Koordinat Y: %s" % (IptKoordinat_Y))

# SECTION 4: Input Koordinat Z
InputKoordinat_Z()
print(Z)
print("Ipt Koordinat Z: %s" % (IptKoordinat_Z))

START.wait_for_press()
lcd.cursor_pos = (0, 0)
lcd.write_string('INPUT X= ')
lcd.cursor_pos = (0, 10)
lcd.write_string(X)
lcd.cursor_pos = (1, 0)
lcd.write_string('INPUT Y= ')
lcd.cursor_pos = (1, 10)
lcd.write_string(Y)
lcd.cursor_pos = (2, 0)
lcd.write_string('INPUT Z= ')
lcd.cursor_pos = (2, 10)
lcd.write_string(Z)
lcd.cursor_pos(3, 0)
lcd.write_string("START=INPUTAN KEDUA")
time.sleep(2)
Formulasi()

START.wait_for_press()
print('Selesai')

# SECTION 3: Disconnect Servo and Clean GPIO
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()
GPIO.cleanup()