# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=400, distance=20, then=Stop.BRAKE)
    br.turn(angle=200, speed=400)
    br.turn(angle=-200, speed=-400)

    br.curve(speed=800, radius=300, angle=360)
    for p in range(4):
        br.curve(speed=800, radius=100, angle=45)
        br.curve(speed=800, radius=100, angle=-45)
        br.curve(speed=800, radius=-100, angle=45)
        br.curve(speed=800, radius=-100, angle=-45)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
