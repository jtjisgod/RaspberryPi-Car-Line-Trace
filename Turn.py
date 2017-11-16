#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 대한 우회전/좌회전 모듈
"""

import R
from Run import *
<<<<<<< HEAD

def right() :
    print ("Right Turn")
    LeftMotor(1)
    RightMotor(0)
    LeftPwm.ChangeDutyCycle(R.speed)
    RightPwm.ChangeDutyCycle(R.speed)

def left() :
    print ("Left Turn")
    LeftMotor(0)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed)
    RightPwm.ChangeDutyCycle(R.speed)

def smallRight() :
    print ("smallRight")
    LeftMotor(1)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed)
    RightPwm.ChangeDutyCycle(R.speed*0.8)

def smallLeft() :
    print ("smallLeft")
    LeftMotor(1)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed*0.8)
    RightPwm.ChangeDutyCycle(R.speed)
=======
speed2 = 50
def right() :
    print ("Right Turn")

def left() :
    print ("Left Turn")

def smallRight() :
    print ("smallRight")
    go_forward_any(10)
    LeftPwm.ChangeDutyCycle(speed2*1.3)
    sleep()
def smallLeft() :
    print ("smallLeft")
    go_forward_any(10)
    RightPwm.ChangeDutyCycle(speed2*1.3)
    print(speed2)
>>>>>>> c9a978d7deb984b763b04a64f069dcc681258d6e
