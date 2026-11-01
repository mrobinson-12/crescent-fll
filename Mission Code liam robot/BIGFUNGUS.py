# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    print("Battery Percentage: " + str(br.getBatteryPercentage()) + "%")
    br.moveLeftAttachmentMotorUntilStalled(
        speed=250, then=Stop.COAST, duty_limit=26
    )
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=-200)
    br.driveForDistance(speed=200, distance=690, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-300)
    br.driveForDistance(speed=150, distance=-125, then=Stop.BRAKE, gyro=True)
    br.turn(angle=49, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=500, speed=300)
    br.moveLeftAttachmentMotorUntilStalled(
        speed=250, then=Stop.COAST, duty_limit=26
    )
    br.moveLeftAttachmentMotorForMillis(millis=600, speed=-200)
    br.moveLeftAttachmentMotorForMillis(millis=575, speed=-250)
    br.driveForDistance(speed=150, distance=186, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorUntilStalled(
        speed=250, then=Stop.COAST, duty_limit=26
    )
    br.moveLeftAttachmentMotorForMillis(millis=600, speed=-200)
    br.driveForDistance(speed=100, distance=-22, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-5, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=-248)
    br.wait(1300)
    br.moveLeftAttachmentMotorForMillis(millis=700, speed=180)
    br.driveForDistance(speed=200, distance=-80, then=Stop.BRAKE, gyro=True)
    br.turn(angle=27, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorUntilStalled(
        speed=250, then=Stop.COAST, duty_limit=29
    )
    br.driveForDistance(speed=200, distance=180, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2500, speed=-350)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
