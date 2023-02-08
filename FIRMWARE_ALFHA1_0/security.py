"""security.py"""
from machine import Pin
from actuator_constants import *
from display_engine import *
import time


class Security:
    """Security and Alarm System"""

    def __init__(self):
        self.pir = Pin(PIR_SENSOR_PIN, Pin.IN, Pin.PULL_DOWN)
        self.buzzer = Pin(BUZZER_PIN, Pin.OUT)

    def activate_guard_mode(self):
        """Guard Mode"""

        while True:
            look_close()
            open_eyes()
            if self.pir.value() == 1:
                self.buzzer.value(1)
                time.sleep(1)
                self.buzzer.value(0)
                time.sleep(1)
