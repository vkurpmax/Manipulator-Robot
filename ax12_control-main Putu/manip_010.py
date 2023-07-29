from Ax12 import Ax12
from gpiozero import Button
from signal import pause
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
import math

# Declare Variables
a = 0

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
my_dxl_1.set_moving_speed(30)
my_dxl_2.set_moving_speed(30)
my_dxl_3.set_moving_speed(30)

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
    servo_4 = 13            # Using GPIO 13
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
    servo_5 = 12            # Using GPIO 12
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
    global X, Y, Z
    global T1, T2, T3
    
    L1 = 85     # mm
    L2 = 165    # mm
    L3 = 155    # mm
    
    # Formulasi Invers Kinematics Robot Manipulator

    theta1 = math.atan2(Y, X)    # Radian

    h = Z - L1                   
    c3 = (X*X + Y*Y + h*h - L2*L2 - L3*L3) / (2*L2*L3)  # This is cos theta 3
    s3a = -math.sqrt(1 - c3*c3)     # For down elbow
    s3b = math.sqrt(1 - c3*c3)      # For up elbow
    theta3 = math.atan2(s3a, c3)    # Radian

    alfa = math.atan2(math.sin(math.acos(c3)) * L3, L2 + math.cos(math.acos(c3)) * 155)
    beta = math.atan2(h, math.sqrt(X*X + Y*Y))
    theta2 = alfa + beta

    T1a = theta1 * 180.0 / math.pi  # T1a is theta1 in Degree
    T2a = theta2 * 180.0 / math.pi  # T2a is theta2 in Degree
    T3a = theta3 * 180.0 / math.pi  # T3a is theta3 in Degree
  
    T1 = 510 + (T1a / 0.29297)  # Decimal Value
    T2 = 243 + (T2a / 0.29297)  # Decimal Value
    T3 = 460 + (T3a / 0.29297)  # Decimal Value


# - - - - - - - - - - - - - - - - 
# - - - -  MAIN PROGRAM   - - - -
# - - - - - - - - - - - - - - - -
# Position 1:
my_dxl_1.set_goal_position(500)
my_dxl_2.set_goal_position(230)
my_dxl_3.set_goal_position(325)
SetAngle_4(80)
SetAngle_5(180)

InputKoordinat_X()
InputKoordinat_Y()
InputKoordinat_Z()

# Position 2:
my_dxl_1.set_moving_speed(30)
my_dxl_2.set_moving_speed(30)
my_dxl_3.set_moving_speed(30)
my_dxl_1.set_goal_position(500)
my_dxl_2.set_goal_position(400)
my_dxl_3.set_goal_position(325)
time.sleep(3)

Formulasi()

# Position 3:
my_dxl_1.set_moving_speed(30)
my_dxl_2.set_moving_speed(15)
my_dxl_3.set_moving_speed(30)

my_dxl_1.set_goal_position(int(T1))
time.sleep(2)
my_dxl_2.set_goal_position(int(T2))
time.sleep(4)
my_dxl_3.set_goal_position(int(T3))
time.sleep(2)


SetAngle_4(80)
SetAngle_5(140)

print("\nDynamixel 1 Present Position: %d" % (my_dxl_1.get_present_position()))
print("Dynamixel 2 Present Position: %d" % (my_dxl_2.get_present_position()))
print("Dynamixel 3 Present Position: %d" % (my_dxl_3.get_present_position()))
print("")

# Position 4:
my_dxl_2.set_moving_speed(30)
my_dxl_2.set_goal_position(400)
time.sleep(3)

# Position 5:
my_dxl_1.set_moving_speed(30)
my_dxl_2.set_moving_speed(15)
my_dxl_3.set_moving_speed(30)
my_dxl_1.set_goal_position(790)
my_dxl_2.set_goal_position(270)
my_dxl_3.set_goal_position(325)
#SetAngle_5(150)
time.sleep(3)

SetAngle_4(90)
SetAngle_5(180)

# Position 6:
my_dxl_2.set_moving_speed(30)
my_dxl_2.set_goal_position(400)
time.sleep(2)

# Position 7:
my_dxl_1.set_moving_speed(30)
my_dxl_2.set_moving_speed(10)
my_dxl_3.set_moving_speed(30)
my_dxl_1.set_goal_position(500)
my_dxl_2.set_goal_position(280)
my_dxl_3.set_goal_position(325)
time.sleep(6)

    
print("\nClosing Manipulator Program")
print("")

print("T1 : %d" % (T1))
print("T2 : %d" % (T2))
print("T3 : %d" % (T3))

print('Selesai')

lcd.clear()
lcd.cursor_pos = (1, 0)
lcd.write_string('SELESAI')

# SECTION 3: Disconnect Servo and Clean GPIO
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()
GPIO.cleanup()