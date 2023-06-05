# Manipulator-Robot
Log of what I did step by step

## 20230226
No progress. Dynamixel shield doesn't make the servo moved a single degree. I'm frustrated.

## 20230227
- Talk to lecturer for the possibilities of title change. Prefer back to old title, "Internet of Things" than "Deep Learning". One lecturer said to just go on with "Deep Learning".
- There's contact with customer support Digiware. They gave me a document and tutorial regarding the dynamixel shield.
- Buy USB TTL on Tokopedia. We will se later.

## 20230228
- Nothing changed. I'm still waiting for my package (USB TTL).

## 20230302
- Using USB TTL, I try to do recovery using Dynamixel Wizard 2.0 software and scan the dynamixel but my computer read no connection through USB TTL.

## 20230304
- There's movement. I'm success to control Dynamixel AX-12A.
- I found problem that using dynamixel shield. There was problem with my power supply. The voltage was not 12V through TTL pin on Dynamixel shield even though the supply voltage was 12V.
- I also found problem that the baudrate, protocol, and ID was not right.
- I did scanning the dynamixel first to know baudrate, protocol, and ID using U2D2 and software Dynamixel Wizard 2.0.

## 20230306
- I made Grove 4 Pin. I bought 4 pin connectors and assembled it to 4 pin jumper wires. So it will be female jumper wires to female connector. I will use it for my UART (from U2D2/Dynamixel Shield) to USB TTL.

## 20230308
- I contruct a learning path

## 20230309
- I learn [Inverse Kinematics](https://github.com/vkurpmax/Manipulator-Robot/blob/main/Inverse_Kinematics.md)

## 20230311
- Dissamble the robot. Learn the mechanism of mechanical parts.

## 20230312
- Recover and update firmware using Dynamixel Wizard.
- Set IDs for Dynamixel

## 20230313
- Assemble the dynamixel again.
- Learn Inverse Kinematic from [here](https://opentextbooks.clemson.edu/wangrobotics/chapter/inverse-kinematics/).

## 20230328
- I try to move dynamixel using python. It works in a simple way.

## 20230329
- Now I try to modify the code I found.
- I try to move all dynamixel at once.

## 20230330
- I can move 3 dynamixel servos one by one.

## 20230331
- I am able to move 3 dynamixel servos simultanueosly.

## 20230401
- I try to convert all code from last year project (in C++) to python for this project.
- I use SSH to connect to Raspberry pi.
- I use VNC to connect to Raspberry pi.
- Installing RPi.GPIO library.   
First, update the available package version:
```
sudo apt-get update
```

Then, install RPi.GPIO:
```
sudo apt-get install rpi.gpio
```

## 20230402
- Just found that Servo 5 (Tower Pro SG90) is Dead
- Created program to control servo 4 and 5
- Order new SG90

# 20230403
- Convert C++ code to Python

# 20230404
- Verify python code (sector setup for servo 4 and 5)
- Continue to convert C++ to python for start button sector
- Use gpiozero for button. Make sure you are in the home directory and do this.   
```
sudo apt update
```
and install
```
sudo apt install python3-gpizero   
```
- Convert val1
```
val1 = map(426, 0, 1023, 0, 180);
```
This line of code in C++ is using a function called "map" to convert a value from one range to another.

The "map" function takes five arguments, which are separated by commas:

1. The first argument (426) is the value that needs to be mapped.
2. The second argument (0) is the minimum value of the original range.
3. The third argument (1023) is the maximum value of the original range.
4. The fourth argument (0) is the minimum value of the target range.
5. The fifth argument (180) is the maximum value of the target range.
6. The function then returns a new value, which is the original value (426) mapped to the new range (0 to 180). The new value is stored in the variable "val1".

So in this particular case, the code is mapping a value of 426 from a range of 0 to 1023 to a range of 0 to 180.

The result will be:
```
val1 = int((426 - 0) * (180 - 0) / (1023 - 0) + 0)
```
This line of Python code is performing the same calculation as the map() function in C++ that we discussed earlier. It is taking the value 426 and mapping it from the range 0 to 1023 to the range 0 to 180.

The calculation is performed using simple arithmetic operations:

1. (426 - 0) computes the difference between the input value and the minimum value of the original range.
2. (180 - 0) computes the difference between the maximum and minimum values of the target range.
3. (1023 - 0) computes the difference between the maximum and minimum values of the original range.
4. ((426 - 0) * (180 - 0) / (1023 - 0)) computes the proportion of the input value in relation to the original range, and scales it to the target range.
5. +0 adds the minimum value of the target range to the scaled proportion to get the final mapped value.
int() converts the floating-point value to an integer data type.

So, the final value of val1 is an integer that represents the mapped value of 426 in the range 0 to 180.

# 20230405
- Test code part 1.

# 20230406
- Part 1 validation success. Saved as manip_004.py
- Total 94 rows of code.
- Move to LCD: Source: https://rplcd.readthedocs.io/en/stable/installation.html   
install RPLCD directly from PyPI using pip:
```
sudo pip install RPLCD
```
to use I²C, you also need smbus:
```
sudo apt-get install python3-smbus
```
Configure the interface setting for i2c: (additional if not works)
```
sudo raspi-config
```
Go to Interface Options   
Enable I2C   
and then Finish   
: (additional if not works)
```
lsmod | grep i2c
```
to check i2c adress: (additional if not works)
```
i2cdetect -y 1
```
: (additional if not works)
```
sudo apt-get install libi2c-dev
```
: (additional if not works)
```
sudo pip3 install smbus2
```
- Configure Static IP Address:
```
sudo nano /etc/dhcpd.conf
```
write this:
```
interface wlan0
static ip_address=192.168.235/24
```
# 20230407
- Continuing Code Transformation. Part 2 section LCD.

# 20230408
- I found that my Raspi IP address is still changed. So I use Zenmap to resolve this problem.

# 20230409
- Success to try with keypad
- continue part 2 keypad section InputKoordinat_X()

# 20230410
- Continue keypad InputKoordinat_X()

# 20230411
- Continue keypad InputKoordinat_X()
- Finishing Section-2: InputKoordinat_X(). Waiting for validation.

# 20230412
- Part 2 Validation Complete. 203 Rows of code. Saved as manip_005.py

# 20230413
- Ready to continue to part 3.

# 20230415
- Continue to Section 3: InputKoordinat_Y()
- Finishing Section-3: InputKoordinat_Y(). Waiting for validation.
- Validation Section-3 Complete. Total 267 rows of code. Saved as manip_006.py

# 20230416
- Continue to Section-4: InputKoordinat_Z()

# 20230418
- Section-4: Input Koordinat_Z() Complete. Waiting for validation.

# 20230419
- Section-4: Input Koordinat_Z() Validation Complete. Total 329 rows of code. Saved as manip_007.py.
- Move to Section-5: Formulasi()

# 20230420
- Finish Section-5: Formulasi(). Waiting for validation

# 20230421
- Study Inverse Kinematics.

# 20230423
- Section-5: Formulasi. Code Validation Complete. Total 430 rows of code. Saved as manip_008.py
- Waiting for mathematical verification and validation.

# 20230424
- Section-5: theta1. Mathematical Result is wrong.
- Fixing theta1 display result

# 20230426
- Mathematical Error is fixed validation.

# 20230427
- Continue to Section-6: Gerakan_1().

# 20230502
- Move to Stage-2: Deep Learning
- Order raspberry pi camera
- Section-6: Gerakan_1() validation complete. 466 rows of code. saved as manip_009.py
- Research on deep learning method I will use: Faster R-CNN or YOLO.
- I decided to use YOLO.
- Learn object detection and Instance Segmentation.

# 20230503
- Consider to use Rubik's cube as object.
- Considering to use tennis ball as object.

# 20230505
- Solve VNC resolution problem:   
If you find that raspberry pi resolution is too big using VNC then follow this step:
```
sudo nano /boot/config.txt
```
then uncomment (remove the hashtag) '**#framebuffer_width=1280**' and '**#framebuffer_height=720**' so it will look like this:
```
framebuffer_width=1280
framebuffer_height=720
```
save it, then reboot. After that try to connect again using vnc.

- Camera Setup:
```
pip install opencv-python==4.6.0.66
```
to check if the installation goes right:
```
python
```
```
import cv2
cv2.__version__
quit()
```

# 20230506
- Find Camera coordinat, X, Y, Z

# 20230509
- Package Arducam Camera arrived

# 20230510
- Design camera mounting table using autodesk inventor 2023

# 20230511
- Setting Camera Position to the manipulator table

# 20230512
- I got problem with forward kinematics
- Forward kinematic formula has been found.

# 20230513
- Data Collecting

# 20230514
- Successfully draw bounding box, get the X, Y, H, W relatives coordinates.
- Train the model. Dataset only 1. Not success.

# 20230517
- Data Collection and Annotation. Total Now: 10 images

# 20230518
- Data Collection and Annotation. Total Data: 20 images
- Data Collection and Annotation. Total Data: 30 images

# 20230519

# 20230521
- Collecting data 31-40

# 20230522
- Annotating 31-40 data

# 20230524
- Collecting 50 data has completed

# 20230526
Try to work on local
## A. Installing Python
## B. Sublime Text
### 1) Installing tqdm
On Sublime Terminal:
```
pip install tqdm --upgrade
pip install ipykernel
```
### 2) Installing torch cuda
```
pip install torch==2.0.0+cu118 -f https://download.pytorch.org/whl/torch_stable.html
```
# 20230529
- Making RPI mount

# 20230530
- CPU and RAM is not enough for deep learning

# 20230605
- Replacing Raspberry pi 3 Model B to Raspberry Pi 4 Model B 8GB RAM
- Using Zenmap:   
Profile: Ping Scan 
```
nmap -sn 192.168.188.1-255
```