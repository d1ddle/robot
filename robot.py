from sr.robot3 import *
import math

robot = Robot()

#loop in new thread to constantly check position relative to markers and align
markers = robot.camera.see()
anchor_marker = ""
for marker in markers:
    if marker.id > -1 and marker.id < 28 and anchor_marker = "":
        anchor_marker = marker
        marker_align(anchor_marker)

def marker_align(marker):
    mo = marker.orientation
    if mo.roll > math.pi/8 or mo.roll < -(math.pi/8)
        return "roll error! robot must have fallen on one side!"
    if mo.pitch > math.pi/8 or mo.pitch < -(math.pi/8)
        return "pitch error! robot must be tipped forwards/back!"
    
    if mo.yaw < 0:
        rotate_left, new_anchor_marker
    elif mo.yaw > 0:
        rotate_right, new_anchor_marker
    else:
        return "aligned!"

#loop to constantly check whether against a wall, try 3 times, then back off & turn around.

#linear main program to start; move forward

# first motor board, channel 0 to half power forward
robot.motor_board.motors[0].power = 0.5

# motor board "srABC1", channel 1 to half power forward
# using the syntax to access multiple motor boards
robot.motor_boards['srABC1'].motors[1].power = 0.5

for i in range(0,10):
    r5 = round(robot.arduino.pins[A5].analog_read(),2)
    r4 = round(robot.arduino.pins[A4].analog_read(),2)
    r3 = round(robot.arduino.pins[A3].analog_read(),2)
    print(f"Rear: {r5} Gripper: {r4} {r3}")
    robot.sleep(0.2)

# sleep for 2 second
#robot.sleep(2)

# first motor board, channel 0 to stopped
robot.motor_board.motors[0].power = 0

# first motor board, channel 1 to stopped
robot.motor_board.motors[1].power = 0
