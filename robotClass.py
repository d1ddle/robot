import sr.robot3

## colours
#Colour.OFF
#Colour.RED
#Colour.YELLOW
#Colour.GREEN
#Colour.CYAN
#Colour.BLUE
#Colour.MAGENTA
#Colour.WHITE

class MyRobot(sr.robot3.Robot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.robot = super()
        self.motors = super().motor_board.motors
        self.motors[0].power = 0.4
        self.motors[1].power = -0.4
        self.robot.sleep(5)
        self.camera = super().camera

#init
robot = MyRobot(wait_for_start=False)
power = robot.power_board
motors = robot.motor_board.motors
power.outputs.power_on()

voltage = power.battery_sensor.voltage
current = power.battery_sensor.current
print(f"BATT VOLT: {voltage}, CURRENT: {current}")
if voltage < 10.5:
    print("VOLTAGE TOO LOW")

#power.piezo.buzz(Note.C6, 2, blocking=True)

done = False
mp = 0.4 #motor power
td = 0.72 #turn duration
sd = 2 #straight line/rect width duration
ld = 3 #rect length duration
wt = 2 #wait time

def line(mp, sd, wt):
    motors[0].power = mp
    motors[1].power = mp
    robot.sleep(sd)
    motors[0].power = 0
    motors[1].power = 0
    robot.sleep(wt)

def turnL(mp, td, wt):
    motors[0].power = -mp
    motors[1].power = mp
    robot.sleep(td)
    motors[0].power = 0
    motors[1].power = 0
    robot.sleep(wt)

def oneCircuit():
    line(mp, sd, wt)
    turnL(mp, td, wt)
    
    line(mp, ld, wt)
    turnL(mp, td, wt)
    
    line(mp, sd, wt)
    turnL(mp, td, wt)
    
    line(mp, ld, wt)
    turnL(mp, td, wt)

while not done:
    oneCircuit()
    oneCircuit()
    oneCircuit()
    
#shutdown
power.outputs.power_off()
print("DONE")
