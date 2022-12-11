"""actuator_constants.py"""
from machine import Pin

legServoName = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
legServo = [2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15]
# legAngle=["090","090","090","090","090","090","090","090","090","090","090","090"]
legAngle = ["090", "070", "050", "080", "120", "118", "120", "060", "040", "090", "120", "118"]
led = Pin(25, Pin.OUT)
led.high()
