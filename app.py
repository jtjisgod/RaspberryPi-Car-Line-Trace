#coding:utf-8
"""
    @ Author :
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱을 위한 메인 코드
"""
import LineSensor
import R

def main() :
    R.forward()
    R.backward()
    R.leftTurn()
    R.rightTurn()
    # LineSensor.LineSensor((0,0,0,0,0))

if __name__ == '__main__':
    main()
