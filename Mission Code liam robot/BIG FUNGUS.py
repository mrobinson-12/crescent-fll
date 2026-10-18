# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    print("Battery Percentage: " + str(br.getBatteryPercentage()) + "%")
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-1000)
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=-200)
    br.wait(2000)
    br.driveForDistance(speed=100, distance=680, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-300)
    br.driveForDistance(speed=100, distance=-50, then=Stop.BRAKE, gyro=True)
    br.turn(angle=60, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=1000)
    br.moveLeftAttachmentMotorForMillis(millis=1200, speed=-250)
    br.driveForDistance(speed=100, distance=90, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=1000)
    br.moveLeftAttachmentMotorForMillis(millis=1200, speed=-1000)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
