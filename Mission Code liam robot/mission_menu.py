"""Run this file on Liam's robot to choose a mission with the hub buttons.

Left/right: choose a number. Middle: run that mission.
After the mission finishes, the menu comes back.

To assign a different .py file:
1. Keep it in this folder and give it a name without spaces or hyphens.
   For example, rename "drone working.py" to "drone_working.py".
2. Add an import below, e.g. import drone_working (leave off .py).
3. Set a number below to its Run function, e.g. "1": drone_working.Run.
4. Download/run this menu again so your changes reach the hub.

Each mission needs def Run(br), just like the existing mission files.
Use single digits 1-9 so each choice fits on the hub display.
"""

from pybricks.tools import hub_menu, wait

from base_robot import BaseRobot
import ant
import dostuff
import Flippything
import revealthething
import thingt
import tree
import treething
import vine


# CHANGE THESE ASSIGNMENTS to choose which .py file each number runs.
MISSIONS = {
    "1": treething.Run,
    "2": revealthething.Run,
    "3": Flippything.Run,
    "4": vine.Run,
    "5": ant.Run,
    "6": thingt.Run,
    "7": tree.Run,
    "8": dostuff.Run,
}


def main():
    br = BaseRobot()

    while True:
        number = str(hub_menu(*MISSIONS))
        # Release the selection button before any mission checks buttons.
        while br.hub.buttons.pressed():
            wait(10)
        br.beep()
        try:
            MISSIONS[number](br)
        finally:
            # Missions may leave a motor running; stop before choosing again.
            br.robot.stop()
            br.leftAttachmentMotor.stop()
            br.rightAttachmentMotor.stop()

        while br.hub.buttons.pressed():
            wait(10)


if __name__ == "__main__":
    main()
