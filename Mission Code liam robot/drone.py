from base_robot import *


def Run(br: BaseRobot):
    br.driveForDistance(distance=600, speed=600, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-800, speed=600, then=Stop.BRAKE, gyro=True)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
