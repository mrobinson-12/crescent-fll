from base_robot import *


def Run(br: BaseRobot):
    for i in range(10):
        br.moveRightAttachmentMotorForMillis(millis=3000, speed=200)

        br.driveForDistance(
            distance=370, speed=100, then=Stop.BRAKE, gyro=True
        )

        br.moveRightAttachmentMotorForMillis(millis=1900, speed=-200)

        # Start attachment WITHOUT waiting
        br.moveRightAttachmentMotorForMillis(
            millis=1000, speed=-200, wait=False
        )

        # Drive while attachment is moving
        br.driveForDistance(
            distance=-130, speed=800, then=Stop.BRAKE, gyro=True
        )
        br.moveRightAttachmentMotorForMillis(millis=2000, speed=200)
        br.driveForDistance(
            distance=130, speed=100, then=Stop.BRAKE, gyro=True
        )
        br.moveRightAttachmentMotorForMillis(millis=1700, speed=-200)

        # Start attachment WITHOUT waiting
        br.moveRightAttachmentMotorForMillis(
            millis=1000, speed=-200, wait=False
        )

        # Drive while attachment is moving
        br.driveForDistance(
            distance=-380, speed=500, then=Stop.BRAKE, gyro=True
        )
        br.wait(1000)


if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
