import sys
from time import sleep
from random import random
import time
import math
sys.path.append("..")
from ax12 import ax12
from select import select
import os
from servoHandler import servoHandler
from switchObj import SwitchObj
import json
from ImPro import ImPro
from FCab import JsonDump

servos = ax12.Ax12()

servoHandlerObj = [0]
servoHandlerObj.append(servoHandler(1, 500, servos))
servoHandlerObj.append(servoHandler(2, 500, servos))
servoHandlerObj.append(servoHandler(3, 500, servos))
servoHandlerObj.append(servoHandler(4, 500, servos))

# - - - - - - - - - - - - - - - - 
# - CHECK MOVE DEMANDED FLAGS - -
# - - - - - - - - - - - - - - - -
def checkMoveDemandedFlags(servoID):
    controlBit = False
    for i in range(len(servoID)):
        if(servoHandlerObj[servoID[i]].moveDemanded):
            return True
    return False

# - - - - - - - - - - - - - - - - 
# - - -  MOVE THEM SERVOS   - - -
# - - - - - - - - - - - - - - - -
def moveThemServos(servoID, pos, speed):
    if isinstance(servoID, list): 
        for index, servo_id in enumerate(servoID):
            servoHandlerObj[servo_id].moveSmooth(pos[index], speed[index])
        while checkMoveDemandedFlags(servoID):
            for i in servoID:
                servoHandlerObj[i].update()
            servos.action()
        sleep(0.1)
    else:
        servoHandlerObj[servoID].moveSmooth(pos, speed)
        while checkMoveDemandedFlags([servoID]):
            servoHandlerObj[servoID].update()
        servos.action()
        sleep(0.1)

# - - - - - - - - - - - - - - - - 
# - - - - - - - - - - - - - - - - 
# - - - MAIN PROG START - - - - -
# - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - 
moveThemServos(1, 800, 200)
moveThemServos(2, 300, 200)
moveThemServos(3, 300, 200)