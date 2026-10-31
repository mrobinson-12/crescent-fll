# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *

# To add auto align for vine


# start all commands with br.
def Run(br: BaseRobot):
    br.moveLeftAttachmentMotorUntilStalled(
        speed=200, then=Stop.HOLD, duty_limit=26
    )
    br.driveForDistance(speed=100, distance=250, then=Stop.BRAKE, gyro=True)
    br.turn(angle=55, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=685, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-56, speed=100, then=Stop.BRAKE, gyro=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-250, wait=False)
    br.driveForDistance(speed=380, distance=100, gyro=True)
    br.driveForDistance(speed=30, distance=20, gyro=True)
    wait(100)
    br.driveForDistance(speed=100, distance=-150, then=Stop.BRAKE)
    br.moveLeftAttachmentMotorForMillis(millis=1500, speed=200, wait=True)
    br.moveLeftAttachmentMotorForMillis(millis=2000, speed=-200, wait=False)
    # Ant
    br.turn(angle=45, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=290, then=Stop.BRAKE, gyro=True)
    br.turn(angle=45, speed=100, then=Stop.BRAKE, gyro=True)
    drive_limits = br.robot.distance_control.limits()
    try:
        br.robot.distance_control.limits(torque=drive_limits[2] * 1.5)
        br.driveForDistance(
            speed=100, distance=380, then=Stop.BRAKE, gyro=True
        )
    finally:
        br.robot.distance_control.limits(*drive_limits)
    br.turn(angle=-45, speed=100, then=Stop.BRAKE, gyro=True)
    # Allow 50% more drive torque for this final push only.
    drive_limits = br.robot.distance_control.limits()
    try:
        br.robot.distance_control.limits(torque=drive_limits[2] * 1.5)
        br.driveForDistance(speed=50, distance=130, then=Stop.BRAKE, gyro=True)
    finally:
        br.robot.distance_control.limits(*drive_limits)
    # Reveal thing
    br.driveForDistance(speed=100, distance=-100, then=Stop.BRAKE, gyro=True)
    br.turn(angle=90, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=300, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=-50, then=Stop.BRAKE, gyro=True)
    br.turn(angle=-30, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=200, then=Stop.BRAKE, gyro=True)
    br.turn(angle=45, speed=100, then=Stop.BRAKE, gyro=True)
    br.driveForDistance(speed=100, distance=350, then=Stop.BRAKE, gyro=True)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
