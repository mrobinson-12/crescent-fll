"""Run this file on Liam's robot to choose a mission with the hub buttons.

Left/right: choose a number. Middle: run that mission.
While a mission is running, press middle to stop it and return to the menu.
After the mission finishes, the menu comes back too.

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
from pybricks.parameters import Button

from base_robot import BaseRobot
import Run1
import Run2
import keystone
import BIGFUNGUS

# CHANGE THESE ASSIGNMENTS to choose which .py file each number runs.
MISSIONS = {
    "1": Run1.Run,
    "2": Run2.Run,
    "3": keystone.Run,
    "4": BIGFUNGUS.Run,
}


def main():
    br = BaseRobot()

    while True:
        try:
            # Let the middle button select a mission instead of stopping it.
            br.hub.system.set_stop_button(None)
            # Reverse navigation while keeping the first mission as the starting choice.
            choices = list(MISSIONS)
            choices = choices[:1] + choices[:0:-1]
            number = str(hub_menu(*choices))
            while br.hub.buttons.pressed():
                wait(10)
            br.beep()
            # Enable the stop button only after the selection button is released.
            br.hub.system.set_stop_button(Button.CENTER)
            MISSIONS[number](br)
            # Disable it before returning to the menu after a normal finish.
            br.hub.system.set_stop_button(None)
        except (KeyboardInterrupt, SystemExit):
            # A stop press ends this mission, not the menu.
            br.hub.system.set_stop_button(None)
        finally:
            br.hub.system.set_stop_button(None)
            # Missions may leave a motor running; stop before choosing again.
            br.robot.stop()
            br.leftAttachmentMotor.stop()
            br.rightAttachmentMotor.stop()

        while br.hub.buttons.pressed():
            wait(10)


if __name__ == "__main__":
    main()
