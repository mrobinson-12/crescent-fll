# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *
def Run(br: BaseRobot):
    br.driveForDistance(
    speed=400, distance=150, then=Stop.BRAKE
)

    br.turn(
    speed=100, angle=90, then=Stop.BRAKE, gyro=True
)

    br.driveForDistance(
    speed=400, distance=100, then=Stop.BRAKE
)

    br.driveForDistance(
    speed=400, distance=-100, then=Stop.BRAKE
)

    br.turn(
    speed=100, angle=-90, then=Stop.BRAKE, gyro=True
)

    br.driveForDistance(
    speed=400, distance=-150, then=Stop.BRAKE
)
# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)

