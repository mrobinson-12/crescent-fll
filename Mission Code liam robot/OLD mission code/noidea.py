# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.turn(angle=-42, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=500, then=Stop.BRAKE, gyro=True)
    br.moveRightAttachmentMotorForMillis(millis=1000, speed=-200, wait=False)
    br.driveForDistance(speed=100, distance=-500, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
