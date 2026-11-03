# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *

# To add auto align for vine


# start all commands with br.
def Run(br: BaseRobot):
    # Aligns attachment
    br.moveLeftAttachmentMotorForMillis(millis=1500, speed=200, wait=True)
    br.moveLeftAttachmentMotorUntilStalled(
        speed=250, then=Stop.HOLD, duty_limit=26
    )
    br.wait(200)
    # makes its way to vine
    br.driveForDistance(speed=250, distance=275, then=Stop.BRAKE, gyro=True)
    br.turn(angle=58, speed=150, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=150, distance=710, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-59, speed=150, then=Stop.BRAKE, gyro=True)
    # pulls vine down
    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-270, wait=False)
    br.driveForDistance(speed=380, distance=115, gyro=True)
    br.driveForDistance(speed=30, distance=20, gyro=True)
    wait(100)
    br.driveForDistance(speed=100, distance=-150, then=Stop.BRAKE)
    br.moveLeftAttachmentMotorForMillis(millis=1500, speed=280, wait=True)
    br.turn(angle=50, speed=250, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-250, wait=True)
    br.driveForDistance(speed=250, distance=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=53, speed=250, then=Stop.BRAKE, gyro=True)
    drive_limits = br.robot.distance_control.limits()
    try:
        br.robot.distance_control.limits(torque=drive_limits[2] * 1.5)
        br.driveForDistance(
            speed=250, distance=370, then=Stop.BRAKE, gyro=True
        )
    finally:
        br.robot.distance_control.limits(*drive_limits)
        br.beep()
    br.turn(angle=-60, speed=250, then=Stop.BRAKE, gyro=True)
    # Allow 50% more drive torque for this final push only.
    drive_limits = br.robot.distance_control.limits()
    try:
        br.robot.distance_control.limits(torque=drive_limits[2] * 1.5)
        br.driveForDistance(speed=50, distance=250, then=Stop.BRAKE, gyro=True)
    finally:
        br.robot.distance_control.limits(*drive_limits)
    # Reveal thing
    br.driveForDistance(speed=250, distance=-150, then=Stop.BRAKE, gyro=True)
    br.turn(angle=93, speed=250, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=300, distance=1000, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
