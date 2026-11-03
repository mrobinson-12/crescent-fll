# AI generated - im sowwy i just too dumb to make myself


from pybricks.tools import hub_menu, wait
from pybricks.parameters import Button

from base_robot import BaseRobot
import Run1
import Run2
import drone
import keystone
import BIGFUNGUS

# CHANGE THESE ASSIGNMENTS to choose which .py file each number runs.
MISSIONS = {
    "1": Run1.Run,
    "2": drone.Run,
    "3": Run2.Run,
    "4": keystone.Run,
    "5": BIGFUNGUS.Run,
}


def main():
    br = BaseRobot()
    # Use numeric order explicitly; the hub may not preserve dictionary order.
    numbers = sorted(MISSIONS, key=int)
    next_number = numbers[0]

    while True:
        number = None
        try:
            # Let the middle button select a mission instead of stopping it.
            br.hub.system.set_stop_button(None)
            # hub_menu starts on its first choice, so put the next number first.
            start = numbers.index(next_number)
            number = str(hub_menu(*(numbers[start:] + numbers[:start])))
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

        if number is not None:
            next_number = numbers[(numbers.index(number) + 1) % len(numbers)]

        while br.hub.buttons.pressed():
            wait(10)


if __name__ == "__main__":
    main()
