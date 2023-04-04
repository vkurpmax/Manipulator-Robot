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