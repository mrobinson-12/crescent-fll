# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *
def Run(br: BaseRobot):
    br.driveForDistance(
    speed=100, distance=2000, then=Stop.BRAKE
)

# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
