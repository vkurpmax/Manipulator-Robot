from Ax12 import Ax12

# e.g 'COM3' windows or '/dev/ttyUSB0' for Linux
Ax12.DEVICENAME = '/dev/ttyUSB0'

Ax12.BAUDRATE = 1_000_000

# sets baudrate and opens com port
Ax12.connect()

# create AX12 instance with ID 10 
my_dxl_1 = Ax12(1)
my_dxl_2 = Ax12(2)
my_dxl_3 = Ax12(3)

my_dxl_1.set_moving_speed(200)
my_dxl_2.set_moving_speed(200)
my_dxl_3.set_moving_speed(200)

# Range of each motor
# 1: 500 - 800
# 2: 170 - 500
# 3: 215 - 790

def user_input():
    """Check to see if user wants to continue"""
    ans = input('Continue? : y/n ')
    if ans == 'n':
        return False
    else:
        return True


def main(motor_object):
    """ sets goal position based on user input """
    bool_test = True
    while bool_test:

        print("\nPosition of dxl ID: %d is %d " %
              (motor_object.id, motor_object.get_present_position()))
        # desired angle input
        input_pos = int(input("goal pos: "))
        motor_object.set_goal_position(input_pos)
        print("Position of dxl ID: %d is now: %d " %
              (motor_object.id, motor_object.get_present_position()))
        bool_test = user_input()

print("\nPosition of dxl ID: %d is %d " %
              (id, get_present_position()))
# desired angle input
input_pos = int(input("goal pos: "))
set_goal_position(input_pos)
print("Position of dxl ID: %d is now: %d " %
      (id, get_present_position()))

# pass in AX12 object
main(my_dxl_1)
main(my_dxl_2)
main(my_dxl_3)

# disconnect
my_dxl_1.set_torque_enable(0)
my_dxl_2.set_torque_enable(0)
my_dxl_3.set_torque_enable(0)
Ax12.disconnect()
