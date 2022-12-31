"""actuator_constants.py"""
from machine import Pin

legServoName = ["L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
legServo = [2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15]
SIT_POS=["110", "090", "110", "090", "090", "090", "090", "090", "090", "090", "090", "090"]
STAND_POS = ["110", "165", "130", "090", "165", "070", "090", "025", "070", "090", "025", "110"]
led = Pin(25, Pin.OUT)
led.high()

