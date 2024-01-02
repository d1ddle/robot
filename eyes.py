from sr.robot3 import *
import math

#init
robot = Robot(wait_for_start=False)
power = robot.power_board
motors = robot.motor_board.motors
power.outputs.power_on()

done=False
while not done:
    markers = robot.camera.see()
    for marker in markers:
        if ((marker.orientation.yaw*180)/math.pi)<-15:
            robot.kch.leds[LED_A].colour = Color.YELLOW
        if -15<((marker.orientation.yaw*180)/math.pi) and ((marker.orientation.yaw*180)/math.pi)<15:
            robot.kch.leds[LED_B].colour = Color.YELLOW
        if ((marker.orientation.yaw*180)/math.pi)>15:
            robot.kch.leds[LED_C].colour = Color.YELLOW

##while not done:
##    if x<-200:
##        LED A BLUE
##    if -200<x<200:
##        LED B YELLOW
##    if x>200:
##        LED C BLUE
