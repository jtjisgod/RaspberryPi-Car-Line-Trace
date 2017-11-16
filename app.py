#coding:utf-8
"""
    @ Author :
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱을 위한 메인 코드
"""

import R

import RPi.GPIO as GPIO
import time
import sys


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

leftmostled=16
leftlessled=18
centerled=22
rightlessled=40
rightmostled=32

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled,   GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)

def main() :
    R.Run.pwm_setup()
    R.LineSensor.init()
    try:
        while True:
            sensor = (GPIO.input(leftmostled), GPIO.input(leftlessled), GPIO.input(centerled), GPIO.input(rightlessled), GPIO.input(rightmostled))
            print("")
            print(sensor)
            if R.huddle() == True :
                continue
            R.LineSensor.chkStatus(sensor)()
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        pwm_low()

def trackingModule() :
    reli = []
    reli.append(GPIO.input(leftmostled))
    reli.append(GPIO.input(leftlessled))
    reli.append(GPIO.input(centerled))
    reli.append(GPIO.input(rightlessled))
    reli.append(GPIO.input(rightmostled))
    return reli

if __name__ == '__main__':
    main()
