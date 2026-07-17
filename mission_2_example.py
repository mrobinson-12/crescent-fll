# Ignore this, this just imports the BaseRobot class, which has the funtions for the robot
# Test script for testing the new functions I make, will be deleted
from base_robot import *
import time


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=9000, distance=1067, then=Stop.BRAKE, gyro=True)
    br.wait(676767)
    br.moveRightAttachmentMotorForDeg(degrees=90, speed=400)
    br.turn(angle=-90, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=500, distance=600, then=Stop.BRAKE, gyro=True)
    br.moveRightAttachmentMotorForDeg(seconds=4)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff
    wait(1)
    br.lightOn
    wait(1)
    br.lightOff


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
