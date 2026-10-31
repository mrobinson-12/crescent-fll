from base_robot import *

# Not accurate enough yet and needs manual intervention - to fix but works


def Run(br: BaseRobot):
    br.leftAttachmentMotor.run_until_stalled(
        150, then=Stop.HOLD, duty_limit=26
    )

    br.moveLeftAttachmentMotorForMillis(millis=1800, wait=False, speed=-190)
    # resets attatchment to up
    br.driveForDistance(distance=300, speed=200, then=Stop.HOLD, gyro=True)
    # drives to mission
    br.moveLeftAttachmentMotorForMillis(millis=1000, speed=400, then=Stop.HOLD)
    # attatchment motor down
    br.leftAttachmentMotor.control.limits(800, 1000, 1000)
    # Start attachment WITHOUT waiting
    br.moveLeftAttachmentMotorForMillis(
        millis=1500, speed=1000, wait=False, then=Stop.HOLD
    )

    # Drive while attachment is moving
    br.driveForDistance(distance=-90, speed=500, then=Stop.BRAKE, gyro=True)
    br.wait(100)
    # waits 0.1s to ensure mission works
    br.moveLeftAttachmentMotorForMillis(millis=1400, speed=-600)
    br.wait(100)
    # attatchment back up
    br.turn(angle=-3, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=80, speed=400, then=Stop.HOLD, gyro=True)
    # Move back into pos
    br.moveLeftAttachmentMotorForMillis(millis=1150, speed=300, then=Stop.HOLD)
    # attatchment down
    br.leftAttachmentMotor.control.limits(1000, 1000, 1000)
    br.wait(150)
    # Start attachment WITHOUT waiting
    br.moveLeftAttachmentMotorForMillis(
        millis=2200, speed=1000, wait=False, then=Stop.HOLD
    )

    # Drive while attachment is moving
    br.driveForDistance(distance=-100, speed=900, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-400, speed=600, then=Stop.BRAKE, gyro=True)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
