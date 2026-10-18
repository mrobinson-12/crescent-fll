"""
This code should not need to be run directly or edited by the students unless they want to add some functions. It is a baserobot class which includes functions, settings, and setup for the robot.
There are variables in here that should be changed to match the configuration of your robot and you can add some extra functions if you would like.
"""

from pybricks.parameters import Color
from pybricks.pupdevices import Motor, ColorSensor

from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Side,
    Stop,
    Color,
    Button,
    Icon,
)
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks import version

# THESE MUST BE CHANGED TO MATCH YOUR ROBOT'S CONFIGURATION
TIRE_DIAMETER = 56  # mm
AXLE_TRACK = 167  # distance between the wheels, mm
COLOR_SENSOR_PORT = Port.D
COLOR_SENSOR_PORT_2 = Port.F
LEFT_DRIVE_MOTOR_PORT = Port.C
RIGHT_DRIVE_MOTOR_PORT = Port.B
LEFT_ATTACHMENT_MOTOR_PORT = Port.A
RIGHT_ATTACHMENT_MOTOR_PORT = Port.E


class BaseRobot:

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
        self.leftDriveMotor = Motor(
            LEFT_DRIVE_MOTOR_PORT, Direction.COUNTERCLOCKWISE
        )
        self.rightDriveMotor = Motor(
            RIGHT_DRIVE_MOTOR_PORT, Direction.CLOCKWISE
        )
        self.robot = DriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
        )

        self.leftAttachmentMotor = Motor(LEFT_ATTACHMENT_MOTOR_PORT)
        self.rightAttachmentMotor = Motor(RIGHT_ATTACHMENT_MOTOR_PORT)

        self.colorSensor = ColorSensor(COLOR_SENSOR_PORT)
        self.colorSensor2 = ColorSensor(COLOR_SENSOR_PORT_2)

    def moveLeftAttachmentMotorForMillis(self, millis, speed, wait=True):
        self.leftAttachmentMotor.run_time(speed, millis, wait=wait)

    def moveRightAttachmentMotorForMillis(
        self,
        millis,
        speed,
        wait=True,
    ):
        self.rightAttachmentMotor.run_time(speed, millis, wait=wait)

    def rightMotorALLUP(
        self,
        speed=300,
        timeout=3000,
    ):
        self.rightAttachmentMotor.run(speed)

        elapsed = 0

        while not self.rightAttachmentMotor.stalled():
            wait(10)
            elapsed += 10

            if elapsed >= timeout:
                self.rightAttachmentMotor.stop()
                return False

        self.rightAttachmentMotor.stop()
        return True

    def moveLeftAttachmentMotorForDeg(
        self,
        degrees,
        speed,
    ):
        self.leftAttachmentMotor.run_angle(
            speed, degrees, then=Stop.BRAKE, wait=True
        )

    def moveRightAttachmentMotorForDeg(
        self,
        degrees,
        speed,
    ):
        self.rightAttachmentMotor.run_angle(
            speed, degrees, then=Stop.BRAKE, wait=True
        )

    def driveForDistance(self, distance, speed, then=Stop.BRAKE, gyro=True):
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_speed=speed, straight_acceleration=500)
        self.robot.straight(distance, then=then)

    def turn(
        self,
        angle,
        speed,
        then=Stop.BRAKE,
        gyro=True,
    ):
        self.robot.use_gyro(gyro)
        self.robot.settings(turn_rate=speed, turn_acceleration=500)
        self.robot.turn(angle, then)

    def lightOn(
        self,
        h,
        s,
        v,
        color=None,
    ):
        self.hub.light.on(Color(h, s, v))

    def wait(
        self,
        time,
    ):
        wait(time)

    def lightOff(self):
        self.hub.light.off()

    def beep(
        self,
        tone=500,
        time=100,
    ):
        self.hub.speaker.beep(tone, time)

    def resetHeading(
        self,
        angle=0,
    ):
        self.robot.reset_heading(angle)

    def curve(
        self,
        radius,
        angle,
        speed=100,
        then=Stop.BRAKE,
        gyro=True,
    ):
        self.robot.use_gyro(gyro)
        self.robot.settings(turn_rate=speed, turn_acceleration=500)
        self.robot.drive(speed, 0)
        self.robot.curve(radius, angle, then)


if __name__ == "__main__":
    print("Don't run the BaseRobot class file. Nothing to do here.")
    print("You probably meant to run one of the mission files.")
