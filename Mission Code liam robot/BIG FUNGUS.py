# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    print("Battery Percentage: " + str(br.getBatteryPercentage()) + "%")
    br.moveLeftAttachmentMotorUntilStalled(
        speed=100, then=Stop.COAST, duty_limit=26
    )
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=-200)
    br.wait(2000)
    br.driveForDistance(speed=100, distance=680, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-300)
    br.driveForDistance(speed=100, distance=-125, then=Stop.BRAKE, gyro=True)
    br.turn(angle=48, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorUntilStalled(
        speed=100, then=Stop.COAST, duty_limit=26
    )
    br.moveLeftAttachmentMotorForMillis(millis=900, speed=-250)
    br.driveForDistance(speed=100, distance=186, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorUntilStalled(
        speed=100, then=Stop.COAST, duty_limit=26
    )
    br.driveForDistance(speed=100, distance=-20, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-5, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=1300, speed=-250)
    br.wait(1300)
    br.moveLeftAttachmentMotorForMillis(millis=700, speed=180)
    br.driveForDistance(speed=100, distance=-200, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=-300, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
