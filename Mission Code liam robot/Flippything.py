from base_robot import *


def Run(br: BaseRobot):
    br.leftAttachmentMotor.run_until_stalled(
        100, then=Stop.HOLD, duty_limit=40
    )

    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-130)
    br.driveForDistance(distance=285, speed=100, then=Stop.BRAKE, gyro=True)

    br.moveLeftAttachmentMotorForMillis(millis=1400, speed=200)

    # Start attachment WITHOUT waiting
    br.moveLeftAttachmentMotorForMillis(millis=500, speed=1000, wait=False)

    # Drive while attachment is moving
    br.driveForDistance(distance=-410, speed=800, then=Stop.BRAKE, gyro=True)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
