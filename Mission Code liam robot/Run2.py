# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *

# To add auto align for vine


# start all commands with br.
def Run(br: BaseRobot):
    br.moveLeftAttachmentMotorUntilStalled(
        speed=200, then=Stop.HOLD, duty_limit=26
    )
    br.driveForDistance(speed=60, distance=250, then=Stop.BRAKE, gyro=True)
    br.turn(angle=54, speed=50, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=60, distance=670, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-56, speed=50, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-270, wait=False)
    br.driveForDistance(speed=385, distance=100, gyro=True)
    br.driveForDistance(speed=30, distance=20, gyro=True)
    wait(100)
    br.driveForDistance(speed=100, distance=-150, then=Stop.BRAKE)
    br.moveLeftAttachmentMotorForMillis(millis=1500, speed=280, wait=True)
    br.turn(angle=40, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-250, wait=True)
    br.turn(angle=-40, speed=100, then=Stop.BRAKE, gyro=True)
    # Ant
    br.turn(angle=50, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=250, then=Stop.BRAKE, gyro=True)
    br.turn(angle=53, speed=100, then=Stop.BRAKE, gyro=True)
    drive_limits = br.robot.distance_control.limits()
    try:
        br.robot.distance_control.limits(torque=drive_limits[2] * 1.5)
        br.driveForDistance(
            speed=100, distance=370, then=Stop.BRAKE, gyro=True
        )
    finally:
        br.robot.distance_control.limits(*drive_limits)
        br.beep()
    br.turn(angle=-60, speed=100, then=Stop.BRAKE, gyro=True)
    # Allow 50% more drive torque for this final push only.
    drive_limits = br.robot.distance_control.limits()
    try:
        br.robot.distance_control.limits(torque=drive_limits[2] * 1.5)
        br.driveForDistance(speed=50, distance=250, then=Stop.BRAKE, gyro=True)
    finally:
        br.robot.distance_control.limits(*drive_limits)
    # Reveal thing
    br.driveForDistance(speed=100, distance=-140, then=Stop.BRAKE, gyro=True)
    br.turn(angle=93, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=350, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=-50, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-30, speed=600, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=800, distance=200, then=Stop.BRAKE, gyro=True)
    br.turn(angle=45, speed=600, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=800, distance=350, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
