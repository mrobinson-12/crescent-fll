from base_robot import *


def Run(br: BaseRobot):
    br.driveForDistance(distance=350, speed=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-20, speed=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-50, speed=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-40, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=50, speed=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=40, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=400, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-200, speed=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-40, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-200, speed=100, then=Stop.BRAKE, gyro=True)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
