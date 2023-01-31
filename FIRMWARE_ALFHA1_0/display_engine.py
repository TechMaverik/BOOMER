"""display engine.py"""

"""
Since OLED display driver shows some anomalities in loading classes. I am writing the display contents 
in a general module
"""
from image_archives import *
from machine import Pin, I2C
from ssd1304_driver import SSD1306_I2C
import framebuf
import time

WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

PI_FRAME_BUFFER = framebuf.FrameBuffer(PI, 32, 32, framebuf.MONO_HLSB)
ARCH_FRAME_BUFFER = framebuf.FrameBuffer(ARCH, 128, 64, framebuf.MONO_HLSB)
OPEN_EYES_FRAME_BUFFER = framebuf.FrameBuffer(OPEN_EYES, 128, 64, framebuf.MONO_HLSB)
CLOSE_EYES_FRAME_BUFFER = framebuf.FrameBuffer(CLOSE_EYES, 128, 64, framebuf.MONO_HLSB)
LOGO_FRAME_BUFFER = framebuf.FrameBuffer(LOGO, 128, 64, framebuf.MONO_HLSB)
SAD_FACE_FRAME_BUFFER = framebuf.FrameBuffer(SAD_FACE, 128, 64, framebuf.MONO_HLSB)
HAPPY_FRAME_BUFFER = framebuf.FrameBuffer(HAPPY, 128, 64, framebuf.MONO_HLSB)
IDLE_FRAME_BUFFER = framebuf.FrameBuffer(IDLE, 128, 64, framebuf.MONO_HLSB)
WATER_FRAME_BUFFER = framebuf.FrameBuffer(WATER, 128, 64, framebuf.MONO_HLSB)


def startup():
    """Startup"""
    oled.fill(0)
    oled.blit(PI_FRAME_BUFFER, 96, 0)
    oled.text("BOOMER V 2.0", 0, 0)
    time.sleep(1)
    oled.show()
    time.sleep(1)
    oled.text("HL", 0, 20)
    oled.text("Robotics", 0, 30)
    oled.text("Project...", 0, 40)
    oled.text("2023", 0, 50)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()
    time.sleep(2)
    oled.text("Built using", 0, 30)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()
    time.sleep(2)
    oled.blit(ARCH_FRAME_BUFFER, 0, 0)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()
    time.sleep(2)
    oled.blit(LOGO_FRAME_BUFFER, 0, 0)
    oled.show()


def blink_eye():
    while True:
        oled.fill(0)
        oled.blit(OPEN_EYES_FRAME_BUFFER, 0, 0)
        oled.show()
        time.sleep(1)
        oled.fill(0)
        oled.blit(CLOSE_EYES_FRAME_BUFFER, 0, 0)
        oled.show()
        time.sleep(1)
