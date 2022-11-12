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
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor,right_motor,55,120)
color_sensor = ColorSensor(Port.S3)
touch_sensor = TouchSensor(Port.S1)
# while not color_sensor.color() == Color.RED:
#     if color_sensor.reflection() < 50:
#         robot.drive(100,50)
#     else:
#         robot.drive(100,-50)
# robot.Stop()
while not color_sensor.color() == Color.RED:
    if color_sensor.reflection() < 10:
        robot.drive(100,70)
    elif color_sensor.reflection() < 50:
        robot.drive(100,50)
    elif color_sensor.reflection() == 50:
        robot.drive(100,0)
    else:
        robot.drive(100,-50)
robot.Stop()
# sei