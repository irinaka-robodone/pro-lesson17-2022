#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (ColorSensor, GyroSensor, InfraredSensor,
                                Motor, TouchSensor, UltrasonicSensor)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor,55, 120)

color_sensor = ColorSensor(Port.S3)
touch_sensor = TouchSensor(Port.S1)

while not color_sensor.color() == Color.RED:
    if color_sensor.reflection() <50:
        robot.drive(100,50)
    elif color_sensor.re
    else:
        robot.drive(100,-50)