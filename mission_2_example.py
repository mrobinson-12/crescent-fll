# Ignore this, this just imports the BaseRobot class, which has the funtions for the robot
# Test script for testing the new functions I make, will be deleted
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=100, distance=100, then=Stop.BRAKE, gyro=True)
    br.wait(1)
    br.moveRightAttachmentMotorForDeg(degrees=90, speed=400)
    br.turn(angle=-90, then=Stop.BRAKE, gyro=True, speed=100)
    br.driveForDistance(speed=100, distance=600, then=Stop.BRAKE, gyro=True)
    br.moveRightAttachmentMotorForDeg(speed=100, degrees=360)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
