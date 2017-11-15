#coding:utf-8
"""
    @ Author : JANGTAEJIN ( jtjisgod@gmail.com )
    @ Date   : 2017-11-13
    @ Body   : 라인트레이싱에 관련된 데이터 집합 모듈
"""

import R
from LineSensorData import LineSensorData
sensorData = []

# LineSensor
def init() :

    print("Init!")

    # Insert test case like under!

    # Foward
    sensorData.append(LineSensorData((2,0,0,0,2), R.forward))
    sensorData.append(LineSensorData((2,0,1,0,2), R.forward))
    sensorData.append(LineSensorData((1,0,0,1,1), R.forward))
    sensorData.append(LineSensorData((1,1,0,0,1), R.forward))
    sensorData.append(LineSensorData((1,1,0,1,1), R.forward))

"""
    # smallRight
    sensorData.append(LineSensorData((2,0,1,1,0), R.rightTurn))

    # turnRight
    sensorData.append(LineSensorData((2,0,0,1,2), R.rightTurn))

    # smallLeft
    sensorData.append(LineSensorData((0,1,1,0,2), R.leftTurn))

    # turnLeft
    sensorData.append(LineSensorData((2,1,0,0,2), R.leftTurn))
"""

def chkStatus(sensor) :
    cbFunc = emptyFunc
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
    pass

if __name__ == '__main__':
    pass
