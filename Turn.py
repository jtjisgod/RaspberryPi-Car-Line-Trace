#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 대한 우회전/좌회전 모듈
"""

import R
from Run import *
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
