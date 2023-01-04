"""actuator_constants.py"""
from machine import Pin

LEG_SERVO_NAME = ["L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
LEG_SERVO_PIN = [2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15]
SIT_POS = [
    "120",
    "090",
    "130",
    "130",
    "100",
    "060",
    "070",
    "090",
    "070",
    "070",
    "090",
    "120",
]
SIT_STAND_TRANSFORMATION_PIN_ARRAY = [3, 6, 11, 14]
SIT_STAND_TRANSFORMATION_PWM_ARRAY = [5000, 8000, 5000, 2000]
STAND_SIT_TRANSFORMATION_PWM_ARRAY = [8000, 5000, 2000, 5000]
INTERVAL = 50
led = Pin(25, Pin.OUT)
led.high()
