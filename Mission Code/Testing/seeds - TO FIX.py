# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=-200, wait=True)
    br.driveForDistance(speed=100, distance=-200, then=Stop.BRAKE)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
