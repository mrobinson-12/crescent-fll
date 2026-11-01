# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    for i in range(10):
        br.moveLeftAttachmentMotorUntilStalled(
            speed=250, then=Stop.COAST, duty_limit=26
        )
        br.moveLeftAttachmentMotorForMillis(millis=i * 100, speed=-200)
        print(i * 100)
        br.wait(500)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
