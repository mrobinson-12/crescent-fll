# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    while True:
        br.turn(angle=280, then=Stop.BRAKE, gyro=True, speed=500)
        br.wait(10000)
        br.driveForDistance(speed=500, distance=100, then=Stop.NONE, gyro=True)
        br.wait(10000)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
