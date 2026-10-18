from base_robot import *


def Run(br: BaseRobot):
    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=50)
    br.moveLeftAttachmentMotorForMillis(millis=880, speed=-300)
    br.driveForDistance(distance=650, speed=100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-39, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=140, speed=600, then=Stop.BRAKE, gyro=True)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
