#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 대한 우회전/좌회전 모듈
"""

import R
import time
from Run import *

# 좌회전을한다
def right() :
    print ("Right Turn")
    LeftMotor(1)
    RightMotor(0)
    LeftPwm.ChangeDutyCycle(R.speed*0.65)
    RightPwm.ChangeDutyCycle(R.speed*0.65)
    """
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)
    #"""

# 우회전을 한다
def left() :
    print ("Left Turn")
    LeftMotor(0)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)
    """
    LeftPwm.ChangeDutyCycle(R.speed*0.7)
    RightPwm.ChangeDutyCycle(R.speed*0.7)
    #"""

# 작은 미세조정을 한다
def smallRight() :
    print ("smallRight")
    LeftMotor(1)
    RightMotor(0)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)

# 작은 미세조정을 한다.
def smallLeft() :
    print ("smallLeft")
    LeftMotor(0)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)
