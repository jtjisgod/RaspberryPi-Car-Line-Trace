#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 관련된 데이터 집합 모듈
"""

import Run
import Turn

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
rightTurn = Turn.right
leftTurn = Turn.left
