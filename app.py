#coding:utf-8
"""
    @ Author :
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱을 위한 메인 코드
"""

import R

def main() :
    R.LineSensor.init()
    print R.LineSensor.chkStatus((0,1,1,0,0))()

    # while True :



if __name__ == '__main__':
    main()
