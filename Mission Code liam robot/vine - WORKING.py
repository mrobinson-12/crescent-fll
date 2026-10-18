# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=100, distance=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=280, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=270, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=250, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=160, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-200, wait=True)
    br.driveForDistance(speed=100, distance=-200, then=Stop.BRAKE)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
