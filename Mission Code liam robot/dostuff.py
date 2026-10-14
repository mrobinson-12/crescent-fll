# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    for i in range(4):
        br.driveForDistance(
            speed=100, distance=1000, then=Stop.NONE, gyro=True
        )


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
