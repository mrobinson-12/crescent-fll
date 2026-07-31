# Ignore this, this just imports the BaseRobot class, which has the functions for the robot
from base_robot import *


# start all commands with br.
def Run(br: BaseRobot):
    for i in range(5):
        br.beep(tone=500, time=80)
        br.beep(tone=750, time=80)
        br.beep(tone=1234, time=80)
        br.beep(tone=2000, time=80)
        br.beep(tone=3000, time=80)
        br.beep(tone=4000, time=80)
        br.beep(tone=5000, time=80)
    for i in range(4):
        br.beep(tone=494, time=115)
        br.beep(tone=784, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=740, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=784, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=740, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=880, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=784, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=740, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=659, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=659, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=740, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=784, time=115)
        br.beep(tone=494, time=115)
        br.beep(tone=880, time=115)


# Ignore everything below this line. This just runs the mission.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)
