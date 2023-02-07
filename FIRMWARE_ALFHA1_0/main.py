"""main.py"""

from movements import MovementMechanism
import communications
from display_engine import *
from message_constants import *
from actuator_constants import *

print(LOADING)
startup()
com_protocol = communications.initialize_communications()
MovementMechanism().action_sitdown_hard()
while True:
    open_eyes()
    close_eyes()
    if com_protocol.any():
        command = com_protocol.read()
        data = str(command.decode()).lower()
        if data == STAND_CMD:
            MovementMechanism().action_transformation_sitdown_standup()
        elif data == SIT_CMD:
            MovementMechanism().action_transformation_standup_to_sitdown()
        elif data == FORWARD_CMD:
            MovementMechanism().action_transformation_stand_forward_stand()
        elif data == ALL_LEGS_UP_CMD:
            MovementMechanism().action_transformation_all_arms_up_down(True)
        elif data == ALL_LEGS_DOWN_CMD:
            MovementMechanism().action_transformation_all_arms_up_down(False)
        elif data == HI_CMD:
            MovementMechanism().action_transformation_say_hi()
