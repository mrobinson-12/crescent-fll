# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *

# To add auto align for vine


# start all commands with br.
def Run(br: BaseRobot):
    br.driveForDistance(speed=100, distance=280, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=280, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=298, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=180, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-200, wait=True)
    br.driveForDistance(speed=100, distance=-200, then=Stop.BRAKE)
    br.moveLeftAttachmentMotorForMillis(millis=3000, speed=-200, wait=True)
    # Ant
    br.turn(angle=45, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=330, then=Stop.BRAKE, gyro=True)
    br.turn(angle=45, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=310, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-45, speed=100, then=Stop.BRAKE, gyro=True)
    # Allow 50% more drive torque for this final push only.
    drive_limits = br.robot.distance_control.limits()
    try:
        br.robot.distance_control.limits(torque=drive_limits[2] * 1.5)
        br.driveForDistance(speed=50, distance=180, then=Stop.BRAKE, gyro=True)
    finally:
        br.robot.distance_control.limits(*drive_limits)
    # Reveal thing
    br.driveForDistance(speed=100, distance=-110, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=300, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-30, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=200, then=Stop.BRAKE, gyro=True)
    br.turn(angle=45, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=300, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
