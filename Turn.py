#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 대한 우회전/좌회전 모듈
"""

import R
from Run import *

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
    RightPwm.ChangeDutyCycle(R.speed*0.5)

def smallLeft() :
    print ("smallLeft")
    LeftMotor(1)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed)
