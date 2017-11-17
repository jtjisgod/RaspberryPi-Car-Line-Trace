#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 대한 전진/후진 모듈
"""


import RPi.GPIO as GPIO # import GPIO librery
import time
import R

GPIO.setmode(GPIO.BOARD)

trig=33
echo=31

#ultrasonic sensor setting
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def getDistance():
    GPIO.output(trig,False)
    time.sleep(0.00001)
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    while GPIO.input(echo)==0:
        pulse_start=time.time()
    while GPIO.input(echo)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17000
    distance=round(distance,2)
    return distance

def huddle() :
    distance = getDistance()
    print "Distance : " + str(distance)
    if distance < 30 :
        print "Stopped"
        R.stop()
        time.sleep(1)

        print "================huddle============"

        turnCount = 0
        while True :
            R.stop()
            if getDistance() > 30 :
                break
            R.right()
            time.sleep(0.25)
            turnCount += 1

        R.forward()
        time.sleep(0.7)

        for i in range(0, turnCount) :
            R.stop()
            getDistance()
            R.left()
            time.sleep(0.25)

        R.forward()
        time.sleep(1)

        while True :
            print "FiveSensor",
            sensor = R.FiveSensor.get()
            print sensor
            if sensor == (1,1,1,1,1) :
                R.left()
                time.sleep(0.1)
                R.forward()
                time.sleep(0.1)
            else :
                break

        while True :
            print "FiveSensor",
            sensor = R.FiveSensor.get()
            print sensor
            if R.LineSensor.cmpStatus(sensor, R.LineSensor.forwardCase) :
                R.right()
                time.sleep(0.1)
                R.forward()
                time.sleep(0.1)
            else :
                break

        R.right()
        time.sleep(0.2)
        R.forward()
        time.sleep(0.2)

        R.stop()

        print "================huddle============"
        return True
    return False
