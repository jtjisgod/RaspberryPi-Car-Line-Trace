#coding:utf-8
"""
    @ Author :
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱을 위한 메인 코드
"""

import R
import FiveSensor
import time
import sys
import RPi.GPIO as GPIO

def main() :
    R.Run.pwm_setup()
    R.LineSensor.init()
    chk = 0
    try:
        while True:
            sensor = FiveSensor.get()
            print("")
            print(sensor)
            if R.huddle() == True :
                continue
            R.LineSensor.chkStatus(sensor)()
            time.sleep(0.06)
            # R.stop()
            chk += 1
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
