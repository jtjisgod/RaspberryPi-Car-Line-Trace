#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 관련된 데이터 집합 모듈
"""

import R
from LineSensorData import LineSensorData
sensorData = []
lastSensor = (2,2,2,2,2)

# LineSensor
def init() :

    print("Init!")
    # Insert test case like under!

    # Foward
    sensorData.append(LineSensorData((1,0,2,0,1), R.forward))
    sensorData.append(LineSensorData((0,0,2,0,0), R.forward))
    sensorData.append(LineSensorData((1,1,2,1,1), R.forward))
    sensorData.append(LineSensorData((0,1,2,1,0), R.forward))
    sensorData.append(LineSensorData((1,1,2,1,1), R.forward))
    #if LineSensorData[0] + [LineSensorData[1] > LineSensorData[3] + LineSensorData[4]:

    # R.smallRight, R.smallLeft = R.smallLeft, R.smallRight
    # R.right, R.left = R.left, R.right

    leftCase = (
     (0,1,1,1,1),
     (2,0,1,1,1),
    );

    smallLeftCase = (
     (1,0,1,1,1),
    );

    for lc in leftCase :
        sensorData.append(LineSensorData(lc, R.left))
        sensorData.append(LineSensorData(lc[-1::-1], R.right))

    for slc in smallLeftCase :
        sensorData.append(LineSensorData(slc, R.smallLeft))
        sensorData.append(LineSensorData(slc[-1::-1], R.smallRight))


    #elif LineSensorData[0] + [LineSensorData[1] < LineSensorData[3] + LineSensorData[4]:

def chkStatus(sensor) :
    global lastSensor
    if sensor == (1,1,1,1,1) :
        sensor = lastSensor;
    lastSensor = sensor
    cbFunc = R.forward
    for data in sensorData :
        score = 0
        for i in range(0, len(data.sensor)) :
            if data.sensor[i] == 2:
                score += 1
                continue
            if sensor[i] == data.sensor[i] :
                score += 1
                continue
        if score == 5 :
            cbFunc = data.callback
            break
    return cbFunc

def emptyFunc() :
    print "EMpty"
    return R.forward

if __name__ == '__main__':
    pass
