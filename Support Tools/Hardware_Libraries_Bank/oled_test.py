from machine import Pin, I2C
from image_archives import *
from ssd1304_driver import SSD1306_I2C
from movements import MovementMechanism
import framebuf
import machine
import utime
import time

WIDTH = 128  # oled display width
HEIGHT = 64  # oled display height
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)  # Init oled display
# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(PI, 32, 32, framebuf.MONO_HLSB)
fb2 = framebuf.FrameBuffer(ARCH, 128, 64, framebuf.MONO_HLSB)
# Clear the oled display in case it has junk on it.
oled.fill(0)
# Blit the image from the framebuffer to the oled display
oled.blit(fb, 96, 0)

# Add some text
oled.text("BOOMER V 2.0", 0, 0)
time.sleep(1)
# Finally update the oled display so the image & text is displayed
oled.show()
time.sleep(1)
oled.text("HL", 0, 20)
oled.text("Robotics", 0, 30)
oled.text("Initiative ..", 0, 40)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()
time.sleep(2)
oled.blit(fb2, 0, 0)
oled.show()
