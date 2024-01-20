from sr.robot3 import *
import math

#init
robot = Robot(wait_for_start=False)
power = robot.power_board
motors = robot.motor_board.motors
power.outputs.power_on()

done=True
done2=False
while not done:
    markers = robot.camera.see()
    for marker in markers:
        print(marker.id, marker.orientation.yaw)
        ## PART A
        passed_b = False
        if marker.orientation.yaw>0.2618: ##more than 15degrees left from square on
            robot.kch.leds[LED_A].colour = Colour.YELLOW
            robot.kch.leds[LED_B].colour = Colour.OFF
            robot.kch.leds[LED_C].colour = Colour.OFF
            print("LED A")
        elif marker.orientation.yaw<0.2618 and not passed_b:
            robot.kch.leds[LED_B].colour = Colour.YELLOW
            robot.kch.leds[LED_A].colour = Colour.OFF
            robot.kch.leds[LED_C].colour = Colour.OFF
            print("LED B, A")
        elif marker.orientation.yaw>-0.2618 and not passed_b: ##middle 30degree arc
            robot.kch.leds[LED_B].colour = Colour.YELLOW
            robot.kch.leds[LED_A].colour = Colour.OFF
            robot.kch.leds[LED_C].colour = Colour.OFF
            print("LED B, B")
        if marker.orientation.yaw<-0.24: ##more than 15degrees right from square on
            passed_b = True
            robot.kch.leds[LED_C].colour = Colour.YELLOW
            robot.kch.leds[LED_B].colour = Colour.OFF
            robot.kch.leds[LED_A].colour = Colour.OFF
            print("LED C")
        if passed_b:
            robot.kch.leds[LED_C].colour = Colour.YELLOW
            robot.kch.leds[LED_B].colour = Colour.OFF
            robot.kch.leds[LED_A].colour = Colour.OFF


while not done2:
    markers = robot.camera.see()
    for marker in markers:
        ## PART B
        ## FOR WHEN ROBOT IS 1metre AWAY FROM MARKER:
        print((marker.position.horizontal_angle*180)/math.pi)
        if ((marker.position.horizontal_angle*180)/math.pi)<-11.31: ##more than 11.31 degrees left of line perpendicular to marker
            robot.kch.leds[LED_C].colour = Colour.BLUE
            robot.kch.leds[LED_B].colour = Colour.OFF
            robot.kch.leds[LED_A].colour = Colour.OFF
        if ((marker.position.horizontal_angle*180)/math.pi)>-11.31 and ((marker.position.horizontal_angle*180)/math.pi)<11.31: ##middle 22.62 degrees; within 200mm of line
            robot.kch.leds[LED_B].colour = Colour.YELLOW
            robot.kch.leds[LED_A].colour = Colour.OFF
            robot.kch.leds[LED_C].colour = Colour.OFF
        if ((marker.position.horizontal_angle*180)/math.pi)>11.31: ##when robot is more than 200mm right of line, aka >11.31 degrees
            robot.kch.leds[LED_A].colour = Colour.BLUE
            robot.kch.leds[LED_B].colour = Colour.OFF
            robot.kch.leds[LED_C].colour = Colour.OFF
