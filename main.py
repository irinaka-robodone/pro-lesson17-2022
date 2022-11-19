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
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, 55, 120)
color_sensor = ColorSensor(Port.S3)
# Write your program here.
ev3.speaker.beep()
# a = 1
# if a>2 robot.turn(-90):
#     else robot.turn(90)
# if a > 2 :
#     robot.turn(-90)
# else:
#     robot.turn(90)
# food ="onigiri" 
# if food == "omusubi":
#     ev3.speaker.beep(440)
# else:
#     ev3.speaker.beep(660)
# score = 75
# if score==100:
#     robot.turn(360)
# elif score>=75:
#     ev3.speaker.beep(5500)
# elif score>50:
#     pass
# else:
#     ev3.screen.print(score)
while not:color_sensor.color() == Color.RED:
    if color_sensor.reflection() > 50:
            robot.drive(100, 90)
    else:
            robot.drive(100, -90)

