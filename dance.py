# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=100, distance=20, then=Stop.BRAKE)
    br.turn(angle=200, speed=400)
    br.turn(angle=-200, speed=-400)
    for i in range(4):
        br.beep(tone=i * 100, time=100)
        br.beep(tone=i, time=100)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
