import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def SetAngle_5(angle):
    servo_5 = 13            # Using GPIO 13
    GPIO.setup(servo_5, GPIO.OUT)
    pwm = GPIO.PWM(servo_5, 50)
    pwm.start(0)
    try:
        while True:
            duty = angle / 18 + 2
            GPIO.output(servo_5, True)
            pwm.ChangeDutyCycle(duty)
            time.sleep(.1)
            #GPIO.output(servo_5, False)
            #pwm.ChangeDutyCycle(0)
    except KeyboardInterrupt:
        
        GPIO.output(servo_5, False)
        pwm.ChangeDutyCycle(0)
        GPIO.cleanup()

SetAngle_5(120)
print('Selesai')
