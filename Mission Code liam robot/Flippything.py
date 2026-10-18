from base_robot import *


def Run(br: BaseRobot):
    br.leftAttachmentMotor.run_until_stalled(
        100, then=Stop.HOLD, duty_limit=30
    )

    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-130)
    br.driveForDistance(distance=290, speed=100, then=Stop.HOLD, gyro=True)

    br.moveLeftAttachmentMotorForMillis(millis=1150, speed=200, then=Stop.HOLD)
    br.leftAttachmentMotor.control.limits(800, 1000, 1000)
    # Start attachment WITHOUT waiting
    br.moveLeftAttachmentMotorForMillis(
        millis=2000, speed=800, wait=False, then=Stop.HOLD
    )

    # Drive while attachment is moving
    br.driveForDistance(distance=-80, speed=800, then=Stop.BRAKE, gyro=True)
    # br.driveForDistance(distance=-400, speed=100, then=Stop.BRAKE, gyro=True)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
