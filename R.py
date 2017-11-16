#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 전체적인 변수 저장
"""

import Run
import Turn
import LineSensor

# MostLeft, Left, Middle, Right, MostRight
lineHandle = {
    'ML' : 0,
    'L' : 1,
    'M' : 2,
    'R' : 3,
    'MR' : 4
}

forward = Run.forward
backward = Run.backward
<<<<<<< HEAD
right = Turn.right
left = Turn.left
=======
rightTurn = Turn.right
leftTurn = Turn.left
>>>>>>> c9a978d7deb984b763b04a64f069dcc681258d6e
smallLeft = Turn.smallLeft
smallRight = Turn.smallRight
stop = Run.stop

<<<<<<< HEAD

speed = 90 # Foward, Backward speed
=======
speed = 10 # Foward, Backward speed
>>>>>>> c9a978d7deb984b763b04a64f069dcc681258d6e
