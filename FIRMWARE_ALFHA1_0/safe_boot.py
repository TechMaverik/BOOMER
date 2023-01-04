"""safe_boot.py"""
from machine import Pin, UART, PWM, I2C
from movements import *
from message_constants import *
from song_bank import *
import actuator_constants as actuator_constants
import movements
import time
# import dht11
uart = UART(0, 9600)

class Safe_Boot:
    """Safe Boot"""
    def __init__(self):
        self.movement_mechanism=movements.MovementMechanism()

    def display_message(self,msg):
        """Display message functionality"""
        print(msg)

    def init_boot(self):
        """initialize boot"""
        self.display_message(BOOT)
        self.movement_mechanism.action_sitdown()
        time.sleep(1)
        self.movement_mechanism.action_transformation_sitdown_standup()
        time.sleep(1)
        self.movement_mechanism.action_transformation_standup_to_sitdown()


Safe_Boot().init_boot()


 
    

