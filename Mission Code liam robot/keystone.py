# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    br.leftAttachmentMotor.run_until_stalled(
        100, then=Stop.COAST, duty_limit=26
    )
    br.wait(200)
    br.moveLeftAttachmentMotorForMillis(millis=1700, speed=-170)
    br.driveForDistance(speed=100, distance=230, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2500, speed=300, wait=False)
    br.turn(angle=45, speed=300, then=Stop.COAST, gyro=True)
    br.wait(2500)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-200, wait=True)

    br.driveForDistance(speed=100, distance=-500, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
