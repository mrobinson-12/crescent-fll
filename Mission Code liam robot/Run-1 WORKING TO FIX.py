from base_robot import *

# Not accurate enough yet and needs manual intervention - to fix but works


def Run(br: BaseRobot):
    br.leftAttachmentMotor.run_until_stalled(
        150, then=Stop.HOLD, duty_limit=26
    )

    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-130)
    br.driveForDistance(distance=295, speed=400, then=Stop.HOLD, gyro=True)

    br.moveLeftAttachmentMotorForMillis(millis=1150, speed=200, then=Stop.HOLD)
    br.leftAttachmentMotor.control.limits(800, 1000, 1000)
    # Start attachment WITHOUT waiting
    br.moveLeftAttachmentMotorForMillis(
        millis=1000, speed=800, wait=False, then=Stop.HOLD
    )

    # Drive while attachment is moving
    br.driveForDistance(distance=-80, speed=800, then=Stop.BRAKE, gyro=True)
    br.wait(1000)
    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-130)
    br.driveForDistance(distance=75, speed=530, then=Stop.HOLD, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=1150, speed=200, then=Stop.HOLD)
    br.leftAttachmentMotor.control.limits(1000, 1000, 1000)
    br.wait(500)
    # Start attachment WITHOUT waiting
    br.moveLeftAttachmentMotorForMillis(
        millis=2000, speed=800, wait=False, then=Stop.HOLD
    )

    # Drive while attachment is moving
    br.driveForDistance(distance=-100, speed=700, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-300, speed=800, then=Stop.BRAKE, gyro=True)
    # br.driveForDistance(distance=-400, speed=100, then=Stop.BRAKE, gyro=True)

    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.wait(3000)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-800, wait=True)
    # Drone
    br.driveForDistance(distance=350, speed=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-20, speed=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-50, speed=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-40, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=50, speed=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=40, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=350, speed=600, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-100, speed=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=10, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(distance=-500, speed=300, then=Stop.BRAKE, gyro=True)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
