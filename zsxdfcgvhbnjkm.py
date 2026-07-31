# Ignore this, this just imports the BaseRobot class, which has the funtions for the robot
# Test script for testing the new functions I make, will be deleted
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    for y in range(3):
        br.turn(angle=90, speed=200)
        br.turn(angle=-90, speed=200)
    # for i in range(4):
    # br.beep(tone=i * 78)
    br.curve(speed=300, radius=360, angle=360)
    br.curve(speed=500, radius=90, angle=90)
    for p in range(4):
        br.curve(speed=400, radius=100, angle=45)
        br.curve(speed=400, radius=100, angle=-45)
        br.curve(speed=400, radius=-100, angle=45)
        br.curve(speed=400, radius=-100, angle=-45)
    # br.beep(tone=2000, time=100)
    br.lightOn(h=34, s=50, v=72)
    # br.lightOn(h=200, s=200, v=200)


# br.lightOn(h=300, s=300, v=300)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
