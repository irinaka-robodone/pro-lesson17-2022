#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

"""
ロボットを定義する
DriveBase(左モーター, 右モーター, タイヤの直径, 車幅)
"""
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 55, 120)

"""
センサーを定義する
"""
color_sensor = ColorSensor(Port.S3)
touch_sensor = TouchSensor(Port.S1)

"""
ライントレース
1. OnOff 制御
2. P制御
"""
while True:
    if color_sensor.reflection() < 50:      # 反射光の大きさが小さい時
        robot.drive(100, 50)
    else:                                   # else: ではなければ
        robot.drive(100, -50)

while not color_sensor.color() == Color.RED:
    if color_sensor.reflection() < 50:      # 反射光の大きさが小さい時
        robot.drive(100, 50)
    elif color_sensor.reflection() = 50: # 前の条件を満たしてなくてもし50なら
        robot.drive(100, 0)
    else:                                   # 前の条件のどれでもなければ
        robot.drive(100, -50)
    
robot.stop()
