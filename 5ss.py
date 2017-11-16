######################################################################
### Date: 2017/11/8
### file name: movement.py
### Purpose: This code has been generated for define
###          going forward and backward.
######################################################################

import RPi.GPIO as GPIO
from time import sleep
import time

# set GPIO warnings as false
GPIO.setwarnings(False)

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# declare the pins of 12, 11, 35 in the Raspberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Raspberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
# =======================================================================
MotorRight_A = 15
MotorRight_B = 13
MotorRight_PWM = 37

# =======================================================================
# set direction
# =======================================================================

left_forward = True
left_backward = False
right_forward = False
right_backward = True


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
def left_motor_direction(direction):
    if direction:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
    elif direction == 0:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
    else:
        print('Config Error')


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorRight_A
# and LOW to HIGH or HIGH to LOW in MotorRight_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorRight_A
# and LOW to HIGH or HIGH to LOW in MotorRight_B
# ===========================================================================
def right_motor_direction(direction):
    if direction:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
    elif direction == 0:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
    else:
        print('Config Error')


# =======================================================================
# because the connections between motors (left motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorLeft_A, GPIO.OUT)
GPIO.setup(MotorLeft_B, GPIO.OUT)
GPIO.setup(MotorLeft_PWM, GPIO.OUT)

# =======================================================================
# because the connections between motors (right motor) and Raspberry Pi has been
# established, the GPIO pins of Raspberry Pi
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
#  go_forward_infinite method has been generated for the three-wheeled moving
#  object to go forward without any limitation of running_time
# =======================================================================
def forward(speedleft,speedright,time):
    # set the left motor to go forward
    left_motor_direction(left_forward)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    right_motor_direction(right_forward)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speedleft)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speedright)
    # set the running time of the left motor to go forward
    sleep(time)

def go_forward(speedleft,speedright,line):
    # set the left motor to go forward
    left_motor_direction(left_forward)
    # GPIO.output(MotorLeft_A,GPIO.HIGH)
    # GPIO.output(MotorLeft_B,GPIO.LOW)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor to go forward
    right_motor_direction(right_forward)
    # GPIO.output(MotorRight_A,GPIO.LOW)
    # GPIO.output(MotorRight_B,GPIO.HIGH)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go forward
    a=70
    b=70
    while True:
        newline=get()
        if newline != line:
            break
        for i in range(10):
            forward(a+(speedleft-a)/10,b+(speedright-b)/10,0.1)

        a=speedleft
        b=speedright
        LeftPwm.ChangeDutyCycle(speedleft)
        # set the speed of the right motor to go forward
        RightPwm.ChangeDutyCycle(speedright)
        # set the running time of the left motor to go forward




# =======================================================================

# =======================================================================
# define the backward module
# backward has the parameters of speed and delay (time)
def go_backward(speed, running_time):
    left_motor_direction(left_forward)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)
    right_motor_direction(right_forward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    time.sleep(running_time)
# =======================================================================

# =======================================================================
# define the stop module
def rightPointTurn(speed, running_time):
    left_motor_direction(left_forward)
    right_motor_direction(right_backward)

    # set the left and right motor pwm to be ready to move
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go backward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the both motors to move
    time.sleep(running_time)


def leftPointTurn(speed, running_time):
    right_motor_direction(right_forward)
    left_motor_direction(left_backward)

    # set the left and right motor pwm to be ready to move
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the speed of the left motor to go backward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the both motors to move
    time.sleep(running_time)


def sleep1(running_time):
    left_motor_direction(left_forward)
    GPIO.output(MotorLeft_PWM, GPIO.LOW)
    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    right_motor_direction(right_forward)
    GPIO.output(MotorRight_PWM, GPIO.HIGH)
    # set the speed of the left motor to go fowrard
    LeftPwm.ChangeDutyCycle(0)
    # set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(0)
    time.sleep(running_time)


def rightSwingTurn(speed, running_time):
    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # set the left motor to go forward
    left_motor_direction(left_forward)

    # set the left motor pwm to be ready to go forward
    GPIO.output(MotorLeft_PWM, GPIO.HIGH)

    # set the right motor pwm to be ready to stop
    # Turn Off Right PWM
    GPIO.output(MotorRight_PWM, GPIO.LOW)
    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to stop
    RightPwm.ChangeDutyCycle(0)
    # set the running time of the left motor to go forward
    time.sleep(running_time)

def leftSwingTurn(speed, running_time):
    # set the left motor pwm to be ready to stop
    # Turn Off Left PWM
    GPIO.output(MotorLeft_PWM, GPIO.LOW)

    # set the right motor to go forward
    right_motor_direction(right_forward)

    # set the right motor pwm to be ready to go forward
    GPIO.output(MotorRight_PWM, GPIO.HIGH)

    # set the speed of the left motor to stop
    LeftPwm.ChangeDutyCycle(0)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the right motor to go forward
    time.sleep(running_time)


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
            time.sleep(0.00001)
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

def get():
    line_status = [GPIO.input(leftmostled),GPIO.input(leftlessled), GPIO.input(centerled),
                   GPIO.input(rightlessled),GPIO.input(rightmostled)]
    return line_status

try:
    while True:
        LeftPwm.start(0)
        RightPwm.start(0)

        sleep(1)

        line =get()

        if line == ['0', '1', '1', '1', '1']:
            go_forward(15, 100, line)
        elif line == ['1', '0', '1', '1', '1']:
            go_forward(20, 90, line)
        elif line == ['1', '1', '0', '1', '1']:
            go_forward(70, 70, line)
        elif line == ['1', '1', '1', '0', '1']:
            go_forward(90, 20, line)
        elif line == ['1', '1', '1', '1', '0']:
            go_forward(100, 15, line)
        elif line == ['0', '0', '1', '1', '1']:
            go_forward(30, 100, line)
        elif line == ['1', '0', '0', '1', '1']:
            go_forward(70, 60, line)
        elif line == ['1', '1', '0', '0', '1']:
            go_forward(60, 70, line)
        elif line == ['1', '1', '1', '0', '0']:
            go_forward(100, 30, line)
        elif line == ['1', '1', '0', '0', '0']:
            go_forward(55, 70, line)
        elif line == ['1', '0', '0', '0', '1']:
            go_forward(70, 70, line)
        elif line == ['0', '0', '0', '1', '1']:
            go_forward(70, 55, line)
        elif line == ['1', '1', '1', '1', '1']:
            go_forward(70, 70, line)

        else:
            stop()








except KeyboardInterrupt:
    GPIO.cleanup()

"""" time.sleep(1)
    if line_status[1]==0 and line_status[2]==0:

            if line_status[0]==0:
                go_forward(20,40,0.01)
            elif line_status[4]==0:
                go_forward(50,20,0.01)
            elif line_status[3]==0:
                go_forward(40,20,0.01)
            else:go_forward(20,20,0.01)
        if line_status[1]==0 and line_status[2]==1:
            go_forward(20,40,0.01)
        if line_status[1]==1 and line_status[2]==0:
            go_forward(40,20,0.01)

if line == ['0', '1', '1', '1', '1']:
    go_forward(15, 100, line)
elif line == ['1', '0', '1', '1', '1']:
    go_forward(20, 90, line)
elif line == ['1', '1', '0', '1', '1']:
    go_forward(70, 70, line)
elif line == ['1', '1', '1', '0', '1']:
    go_forward(90, 20, line)
elif line == ['1', '1', '1', '1', '0']:
    go_forward(100, 15, line)
elif line == ['0', '0', '1', '1', '1']:
    go_forward(30, 100, line)
elif line == ['1', '0', '0', '1', '1']:
    go_forward(70, 60, line)
elif line == ['1', '1', '0', '0', '1']:
    go_forward(60, 70, line)
elif line == ['1', '1', '1', '0', '0']:
    go_forward(100, 30, line)
elif line == ['1', '1', '0', '0', '0']:
    go_forward(55, 70, line)
elif line == ['1', '0', '0', '0', '1']:
    go_forward(70, 70, line)
elif line == ['0', '0', '0', '1', '1']:
    go_forward(70, 55, line)
elif line == ['1', '1', '1', '1', '1']:
    go_forward(70, 70, line)
    
if line == ['0', '1', '1', '1', '1']:
    go_forward(15, 100, line)
elif line == ['1', '0', '1', '1', '1']:
    go_forward(20, 90, line)
elif line == ['1', '1', '0', '1', '1']:
    go_forward(70, 70, line)
elif line == ['1', '1', '1', '0', '1']:
    go_forward(90, 20, line)
elif line == ['1', '1', '1', '1', '0']:
    go_forward(100, 15, line)
elif line == ['0', '0', '1', '1', '1']:
    go_forward(30, 100, line)
elif line == ['1', '0', '0', '1', '1']:
    go_forward(70, 60, line)
elif line == ['1', '1', '0', '0', '1']:
    go_forward(60, 70, line)
elif line == ['1', '1', '1', '0', '0']:
    go_forward(100, 30, line)
elif line == ['1', '1', '0', '0', '0']:
    go_forward(55, 70, line)
elif line == ['1', '0', '0', '0', '1']:
    go_forward(70, 70, line)
elif line == ['0', '0', '0', '1', '1']:
    go_forward(70, 55, line)
elif line == ['1', '1', '1', '1', '1']:
    go_forward(70, 70, line)"""