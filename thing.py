# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    voltage = br.hub.battery.voltage()
    percent = (voltage - 6400) / (8400 - 6400) * 100
    


















# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
