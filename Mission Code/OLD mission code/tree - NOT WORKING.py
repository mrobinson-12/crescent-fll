# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    # br.driveForDistance(speed=100, distance=290, then=Stop.BRAKE, gyro=True)
    # br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    # br.driveForDistance(speed=100, distance=280, then=Stop.BRAKE, gyro=True)
    # br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    #  br.driveForDistance(speed=100, distance=280, then=Stop.BRAKE, gyro=True)
    #  br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    # br.driveForDistance(speed=100, distance=180, then=Stop.BRAKE, gyro=True)
    #  br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    #  br.leftAttachmentMotor.control.limits(100, 1000, 1000)
    # br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-100, wait=False)
    # br.driveForDistance(speed=100, distance=160, then=Stop.BRAKE, gyro=True)
    #  br.wait(1000)
    br.leftAttachmentMotor.control.limits(600, 1000, 300)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-600, wait=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
