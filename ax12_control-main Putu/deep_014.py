# Deep Learning libraries:
from ultralytics import YOLO
import cv2
import torch
import numpy as np

# Machine Learning libraries:
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Dynamixel libraries:
from Ax12 import Ax12
from gpiozero import Button
from signal import pause
import RPi.GPIO as GPIO
import time
import math

# LCD libraries
from RPLCD.i2c import CharLCD

# - - - - - - - - - - - - - - - - 
# - - - - - - - SETUP - - - - - -
# - - - - - - - - - - - - - - - -
## GPIO SETUP
#START = Button(16)          # Using GPIO 16

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

#LCD Homepage
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string('  ROBOT MANIPULATOR ')
lcd.cursor_pos = (1, 0)
lcd.write_string('  3 DOF MENGGUNAKAN ')
lcd.cursor_pos = (2, 0)
lcd.write_string('  KECERDASAN BUATAN ')
lcd.cursor_pos = (3, 0)
lcd.write_string('        2023        ')

# - - - - - - - - - - - - - - - - 
# - - - - - - DEFINE  - - - - - -
# - - - - - - - - - - - - - - - -
def SetAngle_4(angle):          
    servo_4 = 13            # Using GPIO 13
    GPIO.setmode(GPIO.BCM)
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

def Formulasi():
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

#################################
########## MAIN PROGRAM #########
#################################
lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string('         SET        ')
lcd.cursor_pos = (2, 0)
lcd.write_string('     START POINT    ')

# Position 1:
my_dxl_1.set_goal_position(500)
my_dxl_2.set_goal_position(230)
my_dxl_3.set_goal_position(325)
SetAngle_4(80)
SetAngle_5(180)

#################################
##### DEEP LEARNING PROCESS #####
#################################
lcd.clear()
lcd.cursor_pos = (1, 0)
lcd.write_string('     MENYALAKAN     ')
lcd.cursor_pos = (2, 0)
lcd.write_string('       KAMERA       ')

import camcapture	# Running camcapture.py

lcd.clear()
lcd.cursor_pos = (1, 0)
lcd.write_string('   MEMULAI PROSES   ')
lcd.cursor_pos = (2, 0)
lcd.write_string('    DEEP LEARNING   ')

model = YOLO('best_002.pt')  # Load model

# Predict captured image using the model
results = model(source='img0000.png',
                conf=0.55,
                save=True,
                save_txt=True,
                show=True,
                show_labels=True)  # predict on an image

for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    probs = result.probs  # Class probabilities for classification outputs

tensor = boxes.xyxy.clone().detach().requires_grad_(True)
x_img = (tensor[1,0].item() + (tensor[1,2].item() - tensor[1,0].item()) / 2) - tensor[0,0].item()
y_img = tensor[0,3].item() - (tensor[1,1].item() + (tensor[1,3].item() - tensor[1,1].item()) / 2)

#print("x_img: %.1f" % (x_img))
#print("y_img: %.1f" % (y_img))

####################################
##### MACHINE LEARNING PROCESS #####
####################################
lcd.clear()
lcd.cursor_pos = (1, 0)
lcd.write_string('   MEMULAI PROSES   ')
lcd.cursor_pos = (2, 0)
lcd.write_string('  MACHINE LEARNING  ')

# Store the data into a data frame
df = pd.read_csv('tb_manip.csv')

# Take corresponding data into variables
xdata_img = np.array(df['x_img'])
ydata_img = np.array(df['y_img'])
xdata_manip = np.array(df['x_manip'])
ydata_manip = np.array(df['y_manip'])

# Reshape the data for sklearn
xdata_img = xdata_img.reshape((-1, 1))
ydata_img = ydata_img.reshape((-1, 1))
xdata_manip = xdata_manip.reshape((-1, 1))
ydata_manip = ydata_manip.reshape((-1, 1))

### FOR X MODEL ###
# Create a linear regression object
model = LinearRegression()
# Fit the model
model1 = model.fit(xdata_img, xdata_manip)


### FOR Y MODEL ###
# Create a linear regression object
model = LinearRegression()
# Fit the model
model2 = model.fit(ydata_img, ydata_manip)

# Predict images values into manipulator values
x_manip_pred = model1.predict(np.array([[x_img]]))
y_manip_pred = model2.predict(np.array([[y_img]]))
x_manipulator = round(x_manip_pred[0, 0])
y_manipulator = round(y_manip_pred[0, 0])

print("x_manipulator: %d" % (x_manipulator))
print("y_manipulator: %d" % (y_manipulator))

lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string('     TERDETEKSI    ')
lcd.cursor_pos = (2, 0)
lcd.write_string('x = %s' % (str(x_manipulator)))
lcd.cursor_pos = (3, 0)
lcd.write_string('y = %s' % (str(y_manipulator)))

###############################
##### MANIPULATOR PROCESS #####
###############################

X = x_manipulator
Y = y_manipulator
Z = 15

Formulasi()

# IF T1, T2, T3 not
def check_ranges():
    global T1, T2, T3
    # Check if a is inside range 1-250
    if 500 <= T1 <= 810:
        # Check if b is inside range 2-30
        if 165 <= T2 <= 450:
            # Check if c is inside range 3-20
            if 215 <= T3 <= 790:
                confirm()
                return True
    return False

def confirm():
    # Position 2:
    print("")
    my_dxl_1.set_moving_speed(30)
    my_dxl_2.set_moving_speed(30)
    my_dxl_3.set_moving_speed(30)
    my_dxl_1.set_goal_position(500)
    my_dxl_2.set_goal_position(400)
    my_dxl_3.set_goal_position(325)
    time.sleep(2)

    # Position 3:
    print("")
    my_dxl_1.set_moving_speed(30)
    my_dxl_2.set_moving_speed(15)
    my_dxl_3.set_moving_speed(30)

    my_dxl_1.set_goal_position(int(T1))
    time.sleep(2)
    my_dxl_2.set_goal_position(int(T2))
    time.sleep(4)
    my_dxl_3.set_goal_position(int(T3))
    time.sleep(2)

    SetAngle_4(90)
    SetAngle_5(140)

    print("\nDynamixel 1 Present Position: %d" % (my_dxl_1.get_present_position()))
    print("Dynamixel 2 Present Position: %d" % (my_dxl_2.get_present_position()))
    print("Dynamixel 3 Present Position: %d" % (my_dxl_3.get_present_position()))

    # Position 4:
    print("")
    my_dxl_2.set_moving_speed(30)
    my_dxl_2.set_goal_position(400)
    time.sleep(2)
    #SetAngle_5(140)
    #SetAngle_5(140)
    #SetAngle_5(140)

    # Position 5:
    print("")
    my_dxl_1.set_moving_speed(30)
    my_dxl_2.set_moving_speed(15)
    my_dxl_3.set_moving_speed(30)
    my_dxl_1.set_goal_position(790)
    my_dxl_2.set_goal_position(270)
    my_dxl_3.set_goal_position(325)
    #SetAngle_5(140)
    time.sleep(3)

    SetAngle_4(90)
    SetAngle_5(180)

    # Position 6:
    print("")
    my_dxl_2.set_moving_speed(30)
    my_dxl_2.set_goal_position(400)
    time.sleep(2)

    # Position 7:
    print("")
    my_dxl_1.set_moving_speed(30)
    my_dxl_2.set_moving_speed(10)
    my_dxl_3.set_moving_speed(30)
    my_dxl_1.set_goal_position(500)
    my_dxl_2.set_goal_position(280)
    my_dxl_3.set_goal_position(325)
    time.sleep(6)    

    print("\nT1 : %d" % (T1))
    print("T2 : %d" % (T2))
    print("T3 : %d" % (T3))


    print("\nDynamixel 1 Temperature: %d °C" % (my_dxl_1.get_temperature()))
    print("Dynamixel 2 Temperature: %d °C" % (my_dxl_2.get_temperature()))
    print("Dynamixel 3 Temperature: %d °C" % (my_dxl_3.get_temperature()))
    print("")

    print("\nClosing Manipulator Program")
    print("")
    print('Selesai\n')

    lcd.clear()
    lcd.cursor_pos = (1, 0)
    lcd.write_string('       SELESAI      ')
    
check_ranges()

# Disconnect: Disconnect Servo and Clean GPIO
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()
GPIO.cleanup()
cv2.destroyAllWindows()