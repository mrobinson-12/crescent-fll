# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=100, distance=600, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-5, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
