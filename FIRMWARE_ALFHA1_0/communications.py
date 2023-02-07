"""communications.py"""
from machine import UART


def initialize_communications():
    """initialize communications"""
    uart = UART(0, 9600)
    return uart
