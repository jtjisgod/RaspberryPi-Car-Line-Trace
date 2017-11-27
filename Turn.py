#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 대한 우회전/좌회전 모듈
"""

"""
편의를 위해 R.py 만 import 하면 많은 Method 를 쓸 수 있게 구축하였습니다.
RPi.GPIO를 가져오면서 GPIO로 새 이름 지정합니다.
"""
import R
import time
from Run import *


def right() :
    """LightMotor는 전진 RightMotor는 후진하게 하여 right포인트턴을 한다."""
    print ("Right Turn")
    LeftMotor(1)
    RightMotor(0)
    LeftPwm.ChangeDutyCycle(R.speed*0.65)
    RightPwm.ChangeDutyCycle(R.speed*0.65)
    """
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)
    #"""

def left() :
    """LightMotor는 후진 RightMotor는 전진하게 하여 left포인트턴을 한다."""
    print ("Left Turn")
    LeftMotor(0)
    RightMotor(1)
    LeftPwm.ChangeDutyCycle(R.speed*0.5)
    RightPwm.ChangeDutyCycle(R.speed*0.5)
    """
    LeftPwm.ChangeDutyCycle(R.speed*0.7)
    RightPwm.ChangeDutyCycle(R.speed*0.7)
    """

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
