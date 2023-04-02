from Ax12 import Ax12
import RPi.GPIO as GPIO
import time

int START = 3

# - - - - - - - - - - - - - - - - 
# - - - - - GPIO SETUP  - - - - -
# - - - - - - - - - - - - - - - -
GPIO.setmode(GPIO.BOARD)

# Servo_4 Setup
servo_4 = 32
GPIO.setup(servo_4, GPIO.OUT)
pwm = GPIO.PWM(servo_4, 50)
pwm.start(0)

# Servo_5 Setup
servo_5 = 33
GPIO.setup(servo_5, GPIO.OUT)
pwm = GPIO.PWM(servo_5, 50)
pwm.start(0)


# - - - - - - - - - - - - - - - - 
# - - - - DYNAMIXEL SETUP - - - -
# - - - - - - - - - - - - - - - -
# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = '/dev/ttyUSB0'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

# create AX12 instance with ID 10 
my_dxl_1 = Ax12(1)
my_dxl_2 = Ax12(2)
my_dxl_3 = Ax12(3)
my_dxl_1.set_moving_speed(150)
my_dxl_2.set_moving_speed(150)
my_dxl_3.set_moving_speed(150)


# - - - - - - - - - - - - - - - - 
# - - - - - - DEFINE  - - - - - -
# - - - - - - - - - - - - - - - -
def SetAngle_4(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_4, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_4, False)
    pwm.ChangeDutyCycle(0)

def SetAngle_5(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_5, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_5, False)
    pwm.ChangeDutyCycle(0)

def user_input():
    """Check to see if user wants to continue"""
    ans = input('Continue? : y/n ')
    if ans == 'n':
        return False
    else:
        return True

def setup_2():
    GPIO.setup(START, GPIO.IN);

# - - - - - - - - - - - - - - - - 
# - - - -  MAIN PROGRAM   - - - -
# - - - - - - - - - - - - - - - -
setup_2()
Tunggu_Start:




""" sets goal position based on user input """
bool_test = True
while bool_test:

    print("\nPosition of dxl ID: %d is %d " %
          (my_dxl_1.id, my_dxl_1.get_present_position()))
    print("\nPosition of dxl ID: %d is %d " %
          (my_dxl_2.id, my_dxl_2.get_present_position()))
    print("\nPosition of dxl ID: %d is %d " %
          (my_dxl_3.id, my_dxl_3.get_present_position()))
    # desired angle input
    input_pos_1 = int(input("goal pos 1: "))
    input_pos_2 = int(input("goal pos 2: "))
    input_pos_3 = int(input("goal pos 3: "))
    my_dxl_1.set_goal_position(input_pos_1)
    my_dxl_2.set_goal_position(input_pos_2)
    my_dxl_3.set_goal_position(input_pos_3)
    print("Position of dxl ID: %d is now: %d " %
          (my_dxl_1.id, my_dxl_1.get_present_position()))
    print("Position of dxl ID: %d is now: %d " %
          (my_dxl_2.id, my_dxl_2.get_present_position()))
    print("Position of dxl ID: %d is now: %d " %
          (my_dxl_3.id, my_dxl_3.get_present_position()))
    bool_test = user_input()

# disconnect
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()

GPIO.cleanup()