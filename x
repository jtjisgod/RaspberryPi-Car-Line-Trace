
 import RPi.GPIO as GPIO
from time import sleep
import time
# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# set GPIO warnings as false
GPIO.setwarnings(False)


# =======================================================================
# REVERSE function to control the direction of motor in reverse
def REVERSE(x):
    if x == 'True':
        return 'False'
    elif x == 'False':
        return 'True'


# =======================================================================

# =======================================================================
# Set the motor's true / false value to go forward.
forward0 = 'True'
forward1 = 'False'
# =======================================================================

# =======================================================================
# Set the motor's true / false value to the opposite.
backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)
# =======================================================================
# =======================================================================
# declare the pins of 12, 11, 35 in the Raspberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled

# (this codes includes
# the initialization the connection between left motor and Raspberry Pi)
# (this codes includes
# the connection between left motor and Raspberry Pi by software)
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Raspberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled

# (this codes includes
# the initialization the connection between right motor and Raspberry Pi
# (this codes includes
# the connection between right motor and Raspberry Pi by software
# =======================================================================

MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

def leftmotor(x):
    if x == 'True':
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    elif x == 'False':
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    else:
        print(
        'Config Error')


def rightmotor(x):
    if x == 'True':
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    elif x == 'False':
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)


# =======================================================================
# because the connections between motors (left motor) and Raspberry Pi will be
# established, the being connected GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================
GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# because the connections between motors (right motor) and Raspberry Pi will be
# established, the being connected GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================
GPIO.setup(MotorRight_A, GPIO.OUT)
GPIO.setup(MotorRight_B, GPIO.OUT)
GPIO.setup(MotorRight_PWM, GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm = GPIO.PWM(MotorLeft_PWM, 100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm = GPIO.PWM(MotorRight_PWM, 100)


# =======================================================================
# define the forward module
# forward has the parameters of speed and running_time
def go_forward(speed, running_time):
    # set the left motor to go forward
    leftmotor(forward0)
    leftmotor(forward1)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    rightmotor(forward0)
    rightmotor(forward1)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(running_time)


# =======================================================================

# =======================================================================
# define the backward module
# backward has the parameters of speed and delay (time)
def go_backward(speed, running_time):
    # set the left motor to go backward
    leftmotor(backward0)
    leftmotor(backward1)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    # set the right motor to go backward
    rightmotor(backward0)
    rightmotor(backward1)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go backward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go backward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go backward
    sleep(running_time)

# =======================================================================

# =======================================================================
# define the stop module
def rightPointTurn(speed, running_time):
    leftmotor(forward0)
    leftmotor(forward1)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    rightmotor(backward0)
    rightmotor(backward1)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go fowrard
    sleep(running_time)
def leftPointTurn(speed, running_time):
    rightmotor(forward0)
    rightmotor(forward1)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    leftmotor(backward0)
    leftmotor(backward1)
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go fowrard
    sleep(running_time)

def sleep1(running_time):
    leftmotor(forward0)
    leftmotor(forward1)
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    rightmotor(backward0)
    rightmotor(backward1)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(0)
    # set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(0)
    sleep(running_time)


def rightSwingTurn(speed, running_time):
# set the left motor to go fowrard
    leftmotor(forward0)
    leftmotor(forward1)

# set the left motor pwm to be ready to go forward
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
# set the right motor pwm to be ready to stop
# Turn Off Right PWM
    rightmotor(forward0)
    rightmotor(forward1)
    GPIO.output(MotorRight_PWM,GPIO.LOW)
# set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(speed)
# set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(0)
# set the running time of the left motor to go fowrard
    sleep(running_time)

def leftSwingTurn(speed, running_time):
# set the left motor to go fowrard
    rightmotor(forward0)
    rightmotor(forward1)

# set the left motor pwm to be ready to go forward
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
# set the right motor pwm to be ready to stop
# Turn Off Right PWM
    leftmotor(forward0)
    leftmotor(forward1)
    GPIO.output(MotorRight_PWM,GPIO.LOW)
# set the speed of the left motor to go fowrard
    RightPwm.ChangeDutyCycle(speed)
# set the speed of the right motor to stop
    LeftPwm.ChangeDutyCycle(0)
# set the running time of the left motor to go fowrard
    sleep(running_time)

def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)


def ultra():
    GPIO.setmode(GPIO.BOARD)

    trig = 33
    echo = 31

    # ultrasonic sensor setting
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)


    while True:
            go_forward(25,0.05)
            GPIO.output(trig, False)
            GPIO.output(trig, True)
            sleep(0.00001)
            pulse_start = 0
            pulse_end = 0
            GPIO.output(trig, False)
            while GPIO.input(echo) == 0:
                pulse_start = time.time()
            while GPIO.input(echo) == 1:
                pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17000
            distance = round(distance, 2)
            if distance < 12:
                break



# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Rapberry Pi
# as the control pins of 5-way trackinmg sensor in order to
# control direction
#
#  leftmostled    leftlessled     centerled     rightlessled     rightmostled
#       16            18              22             40              32
#
# led turns on (1) : trackinmg sensor led detects white playground
# led turns off(0) : trackinmg sensor led detects black line

# leftmostled off : it means that moving object finds black line
#                   at the position of leftmostled
#                   black line locates below the leftmostled of the moving object
#
# leftlessled off : it means that moving object finds black line
#                   at the position of leftlessled
#                   black line locates below the leftlessled of the moving object
#
# centerled off : it means that moving object finds black line
#                   at the position of centerled
#                   black line locates below the centerled of the moving object
#
# rightlessled off : it means that moving object finds black line
#                   at the position of rightlessled
#                   black line locates below the rightlessled  of the moving object
#
# rightmostled off : it means that moving object finds black line
#                   at the position of rightmostled
#                   black line locates below the rightmostled of the moving object
# =======================================================================

leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 40
rightmostled = 32

# =======================================================================
# because the connetions between 5-way tracking sensor and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared as input
#
# =======================================================================

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)

# =======================================================================
# GPIO.input(leftmostled) method gives the data obtained from leftmostled
# leftmostled returns (1) : leftmostled detects white playground
# leftmostled returns (0) : leftmostled detects black line
#
#
# GPIO.input(leftlessled) method gives the data obtained from leftlessled
# leftlessled returns (1) : leftlessled detects white playground
# leftlessled returns (0) : leftlessled detects black line
#
# GPIO.input(centerled) method gives the data obtained from centerled
# centerled returns (1) : centerled detects white playground
# centerled returns (0) : centerled detects black line
#
# GPIO.input(rightlessled) method gives the data obtained from rightlessled
# rightlessled returns (1) : rightlessled detects white playground
# rightlessled returns (0) : rightlessled detects black line
#
# GPIO.input(rightmostled) method gives the data obtained from rightmostled
# rightmostled returns (1) : rightmostled detects white playground
# rightmostled returns (0) : rightmostled detects black line
#
# =======================================================================




try:
    while True:
        print("leftmostled  detects black line(0) or white ground(1): " + str(GPIO.input(leftmostled)))
        print("leftlessled  detects black line(0) or white ground(1): " + str(GPIO.input(leftlessled)))
        print("centerled    detects black line(0) or white ground(1): " + str(GPIO.input(centerled)))
        print("rightlessled detects black line(0) or white ground(1): " + str(GPIO.input(rightlessled)))
        print("rightmostled detects black line(0) or white ground(1): " + str(GPIO.input(rightmostled)))
        time.sleep(1)
        if GPIO.input(leftmostled)==0:
            go_forward(30,1)



except KeyboardInterrupt:
    GPIO.cleanup()

