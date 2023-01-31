"""launch.py"""
import time
from movements import MovementMechanism
from display_engine import *

startup()
MovementMechanism().action_sitdown_hard()
MovementMechanism().action_transformation_sitdown_standup()
MovementMechanism().action_transformation_stand_forward_stand()
MovementMechanism().action_stand_hard()
MovementMechanism().action_transformation_standup_to_sitdown()
blink_eye()
