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
from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
import math

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
my_dxl_1.set_moving_speed(60)
my_dxl_2.set_moving_speed(60)
my_dxl_3.set_moving_speed(60)

my_dxl_2.set_goal_position(358)
my_dxl_3.set_goal_position(409)
my_dxl_1.set_goal_position(512)

def Formulasi():
    global L1, L2, L3
    global h, Z
    global X, Y, theta1
    global c3, s3, s3a, theta3
    global theta2
    global T1a, T2a, T3a
    global T1, T2, T3

    L1 = 85     # mm
    L2 = 165    # mm
    L3 = 155    # mm

    # Formulasi Invers Kinematics Robot Manipulator
    theta1 = math.atan2(Y, X)    # Radian

    h = Z - L1  # mm    # This is for theta3
    c3 = (X*X + Y*Y + h*h - L2*L2 - L3*L3) / (2*L2*L3)  # This is cos theta 3
    s3 = -math.sqrt(1 - c3*c3)  # For down elbow
    s3a = math.sqrt(1 - c3*c3)  # For up elbow
    theta3 = math.atan2(s3, c3) # Radian

    alfa = math.atan2(h , math.sqrt(X*X + Y*Y))
    beta = math.atan2(math.sin(math.acos(c3)) * L3, L2 + math.cos(math.acos(c3)) * 155)
    theta2 = alfa + beta

    T1a = theta1 * 180.0 / math.pi  # Degree    # T1a is theta1 in Degree
    T2a = theta2 * 180.0 / math.pi  # Degree    # T2a is theta2 in Degree
    T3a = theta3 * 180.0 / math.pi  # Degree    # T3a is theta3 in Degree
  
    T1 = 510 + (T1a / 0.29297)
    T2 = 204 + (T2a / 0.29297)
    T3 = 460 + (T3a / 0.29297)

import camcapture	# Running camcapture.py

#################################
##### DEEP LEARNING PROCESS #####
#################################

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
    
#print(boxes.xyxy)

tensor = boxes.xyxy.clone().detach().requires_grad_(True)
x_img = (tensor[1,0].item() + (tensor[1,2].item() - tensor[1,0].item()) / 2) - tensor[0,0].item()
y_img = tensor[0,3].item() - (tensor[1,1].item() + (tensor[1,3].item() - tensor[1,1].item()) / 2)

print("x_img: %.1f" % (x_img))
print("y_img: %.1f" % (y_img))


####################################
##### MACHINE LEARNING PROCESS #####
####################################

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

###############################
##### MANIPULATOR PROCESS #####
###############################

X = x_manipulator
Y = y_manipulator
Z = 15

Formulasi()
time.sleep(2)
my_dxl_1.set_goal_position(int(T1))
time.sleep(2)
my_dxl_2.set_goal_position(int(T2))
time.sleep(2)
my_dxl_3.set_goal_position(int(T3))
time.sleep(2)

k = cv2.waitKey(1)
print("\nEscape hit, closing the app")
    
# SECTION 3: Disconnect Servo and Clean GPIO
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()
GPIO.cleanup()