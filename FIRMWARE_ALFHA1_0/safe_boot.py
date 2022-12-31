"""safe_boot.py"""
from machine import Pin, UART, PWM, I2C
import actuator_constants as actuator_constants
import movements
import time
from ssd1306 import SSD1306_I2C
import framebuf
import buzzer_music_controls as buzzer_music_controls
import emotions

# import dht11
uart = UART(0, 9600)
print("[ BOOMER ALLIGNMENT SETUP INITIALIZATION CONSOLE HARDWARE ]")
song = ["E5", "G5", "A5", "P", "E5", "G5", "B5", "A5", "P", "E5", "G5", "A5", "P", "G5", "E5"]
song3 = ["E5", "G5", "A5"]  # happy
song2 = ["G5", "E5"]  # sad
song4 = ["A5", "A5", "E5", "E5"]

SLEEP_COUNT = 0

#i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
#oled = SSD1306_I2C(128, 64, i2c)

TH = bytearray(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xf0\x00\x00\x00\x00\x00\x00\x03\xff\xd0\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x00\x1f\xff\xfc\x00\x00\x00\x00?\xff\xff\xe0\x00\x00\x00\x00\x00\xff\xff\xff\x80\x00\x00\x00\xff\x80\x0b\xf8\x00\x00\x00\x00\x03\xf4\x01\x7f\xe0\x00\x00\x03\xf0\x00\x00\x0e\x00\x00\x00\x00\x0e\x00\x00\x03\xf8\x00\x00\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\xe8\x00\x00\x00\x00\x00\x00\x02\xfa\x00\x00\x00\x00\x00\x01\xfe\xff\x80\x00\x00\x00\x00\x00?\xaf\xf0\x00\x00\x00\x00\x0f\x80\x07\xf0\x00\x00\x00\x00\x03\xf8\x00~\x00\x00\x00\x00|\x00\x00~\x00\x00\x00\x00\x0f\xc0\x00\x07\x80\x00\x00\x01\xf0\x00\x00\x1f\x00\x00\x00\x00>\x00\x00\x01\xe0\x00\x00\x03\xc0\x00\x00\x07\xc0\x00\x00\x00x\x00\x00\x00\xf8\x00\x00\x0f\x80\x00\x00\x01\xf0\x00\x00\x01\xf0\x00\x00\x00<\x00\x00\x0f\x00\x00\x00\x00\xf8\x00\x00\x03\xe0\x00\x00\x00\x1f\x00\x00>\x00\x00\x00\x00|\x00\x00\x07\xc0\x00\x00\x00\x0f\x00\x00<\x00\x00\x00\x00<\x00\x00\x0f\x80\x00\x00\x00\x07\xc0\x00x\x00\x00\x00\x00\x1f\x00\x00\x1f\x00\x00\x00\x00\x03\xc0\x00\xf0\x00\x00\x00\x00\x1f\x00\x00\x1e\x00\x00\x00\x00\x01\xe0\x01\xf0\x00\x00\x00\x00\x0f\x80\x00>\x00\x00\x00\x00\x01\xf0\x01\xe0\x00\x00\x00\x00\x07\xc0\x00|\x00\x00\x00\x00\x01\xf0\x03\xe0\x00\x00\x00\x00\x07\xc0\x00|\x00\x00\x00\x00\x00\xf0\x03\xe0\x00\x00\x00\x00\x07\xc0\x00|\x00\x00\x00\x00\x00\xf8\x03\xe0\x00\x00\x00\x00\x03\xe0\x00\xf8\x00\x00\x00\x00\x00\xf8\x07\xc0\x00\x00\x00\x00\x03\xe0\x00\xf8\x00\x00\x00\x00\x00|\x07\xc0\x00\x00\x00\x00\x03\xf0\x01\xf8\x00\x00\x00\x00\x00\xfc\x07\xe0\x00\x00\x00\x00\x03\xe0\x00\xf8\x00\x00\x00\x00\x00|\x07\xc0\x00\x00\x00\x00\x03\xf0\x01\xf8\x00\x00\x00\x00\x00\xfc\x07\xe0\x00\x07\xfe\x00\x03\xf0\x01\xf8\x00\x1f\xfc\x00\x00\xfc\x07\xe0\x009\x7f\xc0\x03\xf0\x01\xf8\x00\xff\xa7\x80\x00\xf8\x03\xe0\x00\xe0\x0f\xf0\x07\xe0\x01\xf8\x03\xfe\x00\xe0\x00\xfc\x07\xf0\x01\xc0\x07\xfc\x03\xf0\x00\xfc\x07\xfc\x00p\x01\xf8\x03\xf0\x03\xc0\x07\xfe\x07\xe0\x00\xfc\x0f\xfc\x00x\x01\xf8\x03\xf0\x07\xe0\x1f\xfe\x0f\xe0\x00\xfc\x0f\xff\x00\xfc\x03\xf8\x01\xf8\x07\xfe\xff\xff\x0f\xc0\x00\xfe\x1f\xff\xef\xfc\x03\xf0\x01\xfc\x0f\xff\xff\xff\x1f\xc0\x00\x7f\x1f\xff\xff\xfc\x07\xe0\x00\xfe\x0f\xff\xff\xff\x1f\xc0\x00?\x1f\xff\xff\xfe\x0f\xe0\x00\x7f\x07\xff\xff\xff\x7f\x80\x00?\xdf\xff\xff\xfc\x1f\xc0\x00\x7f\x8f\xff\xff\xff\xff\x00\x00\x1f\xff\xff\xff\xfc?\xc0\x00?\xc7\xff\xff\xff\xfe\x00\x00\x1f\xff\xff\xff\xfc\xff\x80\x00\x1f\xf3\xff\xff\xff\xfe\x00\x00\x0f\xff\xff\xff\xf9\xff\x00\x00\x07\xff\xff\xff\xff\xf8\x00\x00\x03\xff\xff\xff\xff\xfc\x00\x00\x03\xff\xff\xff\xff\xf0\x00\x00\x03\xff\xff\xff\xff\xf8\x00\x00\x01\xff\xff\xff\xff\xe0\x00\x00\x00\xff\xff\xff\xff\xf0\x00\x00\x00\x7f\xff\xff\xff\x80\x00\x00\x00?\xff\xff\xff\xc0\x00\x00\x00\x1f\xff\xff\xfe\x00\x00\x00\x00\x1f\xff\xff\xff\x00\x00\x00\x00\x07\xff\xff\xf8\x00\x00\x00\x00\x03\xff\xff\xf8\x00\x00\x00\x00\x00\x7f\xff\x80\x00\x00\x00\x00\x00\x7f\xff\xa0\x00\x00\x00\x00\x00\x01H\x00\x00\x00\x00\x00\x00\x00\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
# CLOSE EYES
TH2 = bytearray(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x0c\x00\x000\x00\x00\x18\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x18\x00\x00\x18\x00\x000\x00\x00\x00\x00\x00\x00\x06\x00\x000\x00\x00\x0c\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x0f\x80\x00\xf8\x00\x00\x1f\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x18\xf8\x0f\x0e\x00\x00a\xf0\x1f\x18\x00\x00\x00\x00\x00\x00 ?\xfe\x03\x00\x00\xc4_\xfc\x04\x00\x00\x00\x00\x00\x00\x00`\x83\x02\x00\x00\x00\xc1\x06\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xa1\x00\x00\x00\x01\x83\x02\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x81\x80\x00\x00\x01\x83\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
# LOGO
TH3 = bytearray(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xff\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xff\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/\xff\xff\xff\xf0A\x08F1\x08B\x10\x8cb\x10\x00\x1f\xff\xff\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xf8\x07\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xbf\x80\x00\x1f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x03\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xfc\x00\x00\x00\x00\x00?\xff\xfc\x00\x00\x00\x00\x00\x00\x01\xff\x01\x00\x00\x00\x00\xff\xff\xff\xf0\x00\x00\x00\x01\xfc\x00\xff\x00\x7f\xff\x88\x10\xff\xff\xff\xfc\x0c\x00\x00\x0f\xff\x00\xff\x83\xff\xff\xf8\x01\xff\xff\xff\xfc\x00\x01\x80\xff\xff\xc0\x7f\x9f\x9b\xb7~\x07\xff\xff\xff\xfe\x00\x00\x07\xff\xff\xe0\x7f\xfe\xff\xdf\xcf\xcf\xfe\x00\x1f\xfe\x00\x00?\xff\xff\xf8\x1f\xef\xeay\xfb\xef\xf8\x00\x00\xff\x80\x01\xff\xff\xff\xfc\x1f\xbd\xff\xefv\xff\xe0\x00\x00\x1f\x80\x07\xff\xfc\x0f\xfe\x1c\xfc\x9b\xbf\xcf\xd9\xe0\x00\x00\x0f\x80\x0f\xff\xc0\x07\xff\x0f\xc0\x0f\xf6\xfd\xff\xc0\x00\x00\x07\x80?\xfe\x00\x00\xff\x9b\x80\x05\xdf\x87/\x80\x1f\xc0\x00\x02?\xf0\x00\x00\x7f\xff\x00\x03\xf8\x01\xf9\x80\xff\xfc\x00\x00?\xc0\x00\x00?\xf7\x00\x02`\x00\xefC\xff\xff\x00\x00\x7f\x80\x00\x00\x1f\x9c\x00\x01\xf0\x00?\xc7\xff\xff\x80\x00~\x00\x01\xff\x07\xfc\x01\x81\xa0\x00\x16\xff\xff\xff\xf0\x00~\x00\x07\xff\xc1\xec\x03\xf1\xe0\x00\x1f\xbf\xff\xff\xf8\x00|\x00\x0f\xff\xf9\xf8\x0f\xf1\xc0>\x19\xff\xf8?\xfe\x108\x00\x7f\xff\xffo\x0f\xf9\xe0~\x1f\x7f\xe0\x03\xff\xc0\x00\x00\xff\xff\xff\xff\x0f\xf3\xe0\x7f\x17\xdf\x00\x00\xff\xe0\x00\x01\xff\x07\xff\x9b\x83\xf7\xa0\x7f\x1e\xfc\x00\x00\x7f\xf0\x00\x07\xfc\x00\x7f\x7f\xc1\xed\xe0\x7f7\xe0\x00\x00\x0f\xfc\x00\x0f\xf8\x00\x1f\xf7`\x1f\xd0>?`<\x00\x07\xfc\x00\x1f\xf0\x00\x01\x9f\xff\xeax\x00\xef\xc7\xff\x80\x03\xfe\x00?\x80?\xff\xfb]\xff\xff\x03\xf9\x7f\xff\xc0\x01\xfe\x00\x7f\x00\xff\xffo\xffw\xa9\xfe\xdf\xff\xff\xe0\x00~\x01\xff\x01\xff\xff\xfc\xee\xfd\xff\xbb\xf7\x7f\xff\xf0\x80~\x01\xfe\x03\xff\xff\xf7\xbf\x8f\xde\xff\xdf\xff\xff\xfc\x00~\x01\xf8\x07\xf0\x00\x7f\xee\xf6w\xcd\xf9\xf8\x00\xfe\x00<\x01\xf8\x07\xe0\x00\x14\xfd\xff\xbf~\xef\x00\x00\x7f\x00\x10\x01\xf0\x0f\xc0\x00\x0f\xa3\x89\xa9\xf5\xff\x80\x00?\x80\x00\x00p\x0f\x00\x00\x07\xbe\xf5\xe8\x8f7\xff\xe0\x1f\xe0\x00\x00p>\x00\x00\x03\xe3\x95\xa9y\xff\xff\xf8\x0f\xe0\x00\x00\x00>\x00\x00\x00]\x9d\xef\xcb\x1f\x7f\xfc\x0f\xf0\x00\x00\x00|\x00\x00\x00\x7f\xf7\xb9\x7f\xc0\x7f\xff\x03\xf8@\x00\x00|\x00\x00\x00\x12\xfd\xff\xfa\x00\x00?\x01\xfc\x00\x00\x00\xfd\xe0\x1f\x00/\x97\xae\x88\x07A\xdf\x81\xfc\x00\x01\x80\xfa\xd0z\x80\xdd~_p\x16\x82\xeb\x80\xfc\x00\x00\x00\xf6\xd0[c\xad\x01\xe1H\x19\xc2\xd7\x80\xfc\x00\x00\x00\xfa \xddcb\x81\xa9p\x08\x02\xc8\xc0\xf8\x00\x00\x00z\xd0\xa0\x93A\x02Y\xb8\x1fC,\xc0\xf8\x00\x00\x00v\xf0\xc0c\x81\x83\xa94\x11\x81\xd4\xc0x\x00\x00\x08;(\xa0p\xc1e\xd7\xb4.\x86\xeb\xe0p\x00\x02\x00\x04(\xa0\x93A\x05\x98\xba6\x02\xdb\xe0\x00\x02\x00\x00\x0e\xd8\xb9cB\x85\x8f\n\x17\xc6\xeb\xe0\x00\x00\x00\x00\n\xe0Z\xe0\xf3\n\x11\n6\x85,\xf0\x00\x00\x00\x00\n\xd0'\x00-\x07\x8e\n\x19E\xd4\xf0\x00 \x00\x00\x06\xc0\x04\x00\x1c\x00\x06\x00\x16\x01\x0b\xe0\x00\x00\x00\x10@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe0\x02\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)

# SAD FACE
TH4 = bytearray(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x0f\xffP\x00\x00\x00\x00\x00\x00\x00\x00\x0b\xfd\xff\xff\x80\x00;\xbf\x00\x00\x00\x00\x00\x00\x00\x00\xfcW\xd4\x08\x00\x18\x00\xe1\xf0\x00\x00\x00\x00\x00\x00\x07G\xe8\x000\x00\x0c\x00\x1e\x9e\x00\x00\x00\x00\x00\x00<\xb8\x00\x01@\x00\x06\x00\x01\xe3\xc0\x00\x00\x00\x00\x00\xe3\xc0\x00\x03\x80\x00\x03\x00\x00\x1c\xb0\x00\x00\x00\x00\x03\x9e\x00\x00\x0c`\x00\x01\x80\x00\x07X\x00\x00\x00\x00\x0cp\x00\x0000\x00\x01\xc0\x00\x01\xce\x00\x00\x00\x007\xc0\x00\x00\xc0\x10\x00\x02 \x00\x003\x80\x00\x00\x00m\x00\x00\x07\x00\x08\x00\x02\x18\x00\x00\x1c\xc0\x00\x00\x01\xd8\x00\x00\xb8\x00\x0c\x00\x06\x06\x00\x00\x07p\x00\x00\x07\xc0\x00/@\x00\x04\x00\x04\x01\xc0\x00\x01\xb8\x00\x00\x0e\x05w\xd0\x00\x00\x06\x00\x04\x00}\x00\x00l\x00\x009\xf4\xa0\x00\x0f\xfc\x02\x00\x04\x07\xff\xf5\x00\x1b\x00\x00 \x00 \x00\x7f\xff\x82\x00\x04\x1f\xff\xfa\xf4\x07\x80\x00\x00\x00`\x00\xff\xff\xe2\x00\x04\x7f\xff\xf8\x03\xf2\xe0\x00\x00\x00 \x01\xff\xff\xf2\x00\x06\x7f\xff\xfe\x03\x00\xf0\x00\x00\x00 \x03\xff\xe7\xf6\x00\x06\xf8\x1f\xff\x02\x008\x00\x00\x000\x07\xff\x81\xfc\x00\x03\xe0\x0f\xff\x02\x00\x0e\x00\x00\x00\x10\x07\xff\x83\xfc\x00\x01\xf0\x0f\xff\x06\x00\x07\x00\x00\x00\x18\x03\xff\xc7\xf8\x00\x01\xf8?\xff\x0c\x00\x01\x00\x00\x00\x08\x03\xff\xff\xf8\x00\x00\xff\xff\xfe\x08\x00\x00\x00\x00\x00\x0c\x01\xff\xff\xf0\x00\x00\x7f\xff\xfe0\x00\x00\x00\x00\x00\x02\x00\xff\xff\xe0\x00\x00?\xff\xf8`\x00\x00\x00\x00\x00\x01\x80\x7f\xff\xc0\x00\x00\x1f\xff\xf0\x80\x00\x00\x00\x00\x00\x00\xc0\x0f\xff\x00\x00\x00\x07\xff\x07\x00\x00\x00\x00\x00\x00\x008\x00\x08\x00\x00\x00\x00\xd0X\x00\x00\x00\x00\x00\x00\x00\x07A`\x00\x00\x00\x00\x17@\x00\x00\x00\x00\x00\x00\x00\x00]\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00I\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc1\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x94\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03% \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x880\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x11\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xeb\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
# HAPPY
TH5 = bytearray(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfd\x1c\x00\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\xff\xf8\x00\x1f\x80\x00\x00 \x00\x00\x00\x00\x00\x00\x03\xffW\xf8\x00|\x00\x00\x00p\x00\x00\x00\x00\x00\x00\x0f\xa0\x00\xbe\x01\xf4\x00\x00\x008\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x1f\x87\xd0\x00\x00\x00<\x00\x00\x00\x00\x00\x00|\x00\x00\x07\xdf@\x00\x00\x00\x1e\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x01\xfa\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x01\xe0\x00\x80\x00\xdc\x00\x00\x00\x00\x07\x80\x00\x00\x00\x00\x03\x80\x1dP\x00p\x00\x00\x00\x00\x03\xc0\x00\x00\x00\x00\x07\x80@\x0e\x00<\x00\x00\x00\x00\x01`\x00\x00\x00\x00\x06\x00\x80\x01\x00\x1c\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x0e\x01\x00\x00\x80\x0e\x00/\x01\xc0\x00x\x15\x00\x00\x00\x1c\x02\x00\x00@\x07\x03\xff\x01\xf0\x00-\xff\xfc\x00\x00\x1c\x04\x00\x00 \x07?\xfa\x00\xfc\x00\x1f\xff\xff\x80\x00\x18\x04w\xe0\x10\x03\xfe\x80\x00>\x00?@/\xe0\x008\x08\x8f\xf0\x10\x03\xf0\x00\x00\x0f\xc0\xf8\x00\x01\xf0\x008\x08\x06\xd8\x08\x03\x80\x00\x00\x03\xe1\xe0\x00\x00|\x000\x08\x8f\xfc\x00\x01\x80\x00\x00\x00\xff\xc0\x00\x00\x1e\x000\x10\x7f\xfe\x08\x01\xc0\x00\x00\x00?\x00\x00\x00\x0f\x80p\x00;l\x08\x01\x80\x00\x00\x00\x1a\x00\r\xa0\x03\x800\x10o\xfe\x00\x01\xc0\x00\x00\x00<\x00`\x18\x01\xc0p\x10?\xfc\x08\x01\x80\x00\x00\x008\x00\x80\x04\x01\xe00\x00>\xdc\x08\x01\xc0\x00`\x00p\x03\x00\x03\x00p8\x18;\xf4\x00\x03\x80\x00\xfe\x00\xe0\x02\x00\x00\x80p8\x00\x1f\xfc\x08\x01\x80\x00\x7f\xe8\xa0\x04\x00\x00@88\x08\x0fp\x10\x03\x80\x00\x0b\xfe\xe0\x08E@ 8\x18\x04\x03\xc0\x10\x03\x80\x00\x00\xbf\xc0\x08\xbf\xe0 \x18\x1c\x04\x00\x00 \x07\x00\x00\x00\x07\xc0\x11\x0f\xf0\x10\x1c\x1c\x02\x00\x00@\x07\x00\x00\x00\x01\x80\x11\x1e\xd8\x10\x1c\x0e\x01\x00\x00\x80\x0e\x00\x00\x00\x01\x80\x10\x9b\xf8\x00\x0c\x0f\x00\x80\x01\x00\x1c\x00\x00\x00\x03\x80 \x7f\xfc\x10\x1c\x07\x00`\x06\x00\x1c\x00\x00\x00\x03\x80\x00\x7fl\x08\x0c\x03\xc0\x1a\xb0\x008\x00\x00\x00\x01\x80 \xf7\xfc\x10\x0e\x01\xc0\x00\x80\x00\xf0\x00\x00\x00\x03\x80\x10\x7f\xf8\x00\x0c\x00\xf0\x00\x00\x01\xe0\x00\x00\x00\x01\x80\x10]\xb8\x10\x1c\x00x\x00\x00\x03\xc0\x00\x00\x00\x03\x80\x10?\xf8\x10\x0c\x00>\x00\x00\x0f\x00\x00\x00\x00\x01\xc0\x10;\xb0\x10\x1c\x00\x0f\xc0\x00\x7f\x00\x00\x00\x00\x01\xc0\x08\x0f\xe0 \x1c\x00\x07\xfd+\xfc\x00\x00\x00\x00\x00\xc0\x08\x02\x00 8\x00\x00\xff\xff\xe0\x00\x00\x00\x00\x00\xe0\x04\x00\x00@8\x00\x00\x1f\xff\x00\x00\x00\x00\x00\x00\xe0\x02\x00\x00\x80p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x01\x00\x01\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x80\x06\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00`(\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x0f\xa0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x07\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x80\x00\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe0\x00\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x01\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f@\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\xff\xff@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xfd\xfa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00/@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
# IDLE
TH6 = bytearray(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xdb\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe8\x00\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x03\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\xf8\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x03\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x0f\xff\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x7f\xc0_\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\xfc\x00\x03\xf8\x00\x00\x00\x00\x00\x00\x7f\xfd\x00\x00\x00\x00\xf0\x00\x00|\x00\x00\x00\x00\x00\x07\xea\xbf\xe0\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x00\x00>\x01\xff\xf8\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x01\xf0\x07\xff\xfe\x00\x00\x00\x00\x04\x00\x01\x80\x00\x00\x00\x07\x80\x0f\xff\xff\x80\x00\x00\x03\xff\xf8\x00\xc0\x00\x00\x00\x0e\x00\x0f\xff\xff\xc0\x00\x00?\xa5\xff\x00`\x00\x00\x008\x00\x1f\xff\xc7\xe0\x00\x01\xf0\x0f\xff\xc0\x10\x00\x00\x00p\x00\x1f\xff\xe3p\x00\x07\x80?\xff\xf0\x00\x00\x00\x00\xc0\x00\x0f\xff\xff\xb8\x00\x1e\x00?\xf9\xf8\x00\x00\x00\x01\xc0\x00\x07\xff\xff\x98\x008\x00\x7f\xf8\xfc\x00\x00\x00\x03\x00\x00\x07\xff\xff\x0c\x00\xe0\x00\x7f\xfd\xf6\x00\x00\x00\x07\x00\x00\x01\xff\xfe\x0c\x01\xc0\x00?\xff\xf7\x00\x00\x00\x06\x00\x00\x00\x7f\xfc\x0e\x03\x80\x00?\xff\xf3\x00\x00\x00\x0e\x00\x00\x00\x0b\xa0\x06\x03\x00\x00\x1f\xff\xf1\x80\x00\x00\x0c\x00\x00\x00\x00\x00\x06\x06\x00\x00\x07\xff\xe1\x80\x00\x00\x0c\x00\x00\x00\x00\x00\x06\x0e\x80\x00\x01\xff\x81\xc0\x00\x00\x1c\x00\x00\x00\x00\x00\x06\x0c\x00\x00\x00\x00\x00\xc0\x00\x00\x0c\x00\x00\x00\x00\x00\x06\r\x00\x00\x00\x00\x00\xc0\x00\x00\x1c\x00\x00\x00\x00\x00\x06\x0c\x00\x00\x00\x00\x00\xc0\x00\x00\r\x00\x00\x00\x00\x00\x0e\x1c\x00\x00\x00\x00\x00\xc0\x00\x00\x0c\x00\x00\x00\x00\x00\x0e\r\x00\x00\x00\x00\x00\xc0\x00\x00\x0e\x00\x00\x00\x00\x00\x0c\x0c\x00\x00\x00\x00\x01\xc0\x00\x00\x06\x80\x00\x00\x00\x00\x1c\x0e\x00\x00\x00\x00\x01\x80\x00\x00\x07\x00\x00\x00\x00\x00\x18\x06@\x00\x00\x00\x01\x80\x00\x00\x03 \x00\x00\x00\x008\x07\x00\x00\x00\x00\x03\x80\x00\x00\x01\xc8\x00\x00\x00\x00p\x03\x00\x00\x00\x00\x07\x00\x00\x00\x01\xc0\x00\x00\x00\x00\xe0\x03\xa0\x00\x00\x00\x06\x00\x00\x00\x00r\x00\x00\x00\x02\xc0\x01\xc8\x00\x00\x00\x1e\x00\x00\x00\x008\x80\x00\x00\x0b\x80\x00\xe0\x00\x00\x00,\x00\x00\x00\x00\x1e$\x00\x00O\x00\x00:\x80\x00\x00\xb8\x00\x00\x00\x00\x07\x80\x80\x12<\x00\x00\x1e\x10\x00\x02\xe0\x00\x00\x00\x00\x01\xfa\x15\x01\xf0\x00\x00\x07\xc2DO\x80\x00\x00\x00\x00\x00?\xd0\xff\x80\x00\x00\x01\xfc\x91~\x00\x00\x00\x00\x00\x00\x02\xff\xf8\x00\x00\x00\x00\x1f\xff\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
# WATER
TH7 = bytearray(
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\xff\xfa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xfa\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xff\xff\xff\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00?\xff\xff\xff\xff\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x01\xff\xff\xff\xff\xff\xff\xff\xc0\x00\x00\x00\x00\x00\x00\x00\x03\xf8\xff\xff\xff\xff\xff\xf9\xc0\x00\x00\x00\x00\x00\x00\x00\x07\xc3\xff\xdb\xff\xff\xff\xfc`\x00\x00\x00\x00\x00\x00\x00\x06\x0f\xc0\x0b\xff\xff\xff\xfe \x00\x00\x00\x00\x00\x00\x00\x00\x1bx(\x0f\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x1d\x7f\xfc\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\r\x10\x19\x90\x03\xe0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\xa0\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x006P  \x00\x00*0\x00\x00\x00\x00\x00\x00\x00 A\xa0  \x00\x01\xff\xd0\x00\x00\x00\x00\x00\x00\x00\xcc\xc0\x00\xd0 \x00\x07\xff\xf8\x00\x00\x00\x00\x00\x00\x06#\x85\x80\x16/\xd0\x1f\xff\xf8\x00\x00\x00\x00\x00\x00\x18 \x88\x00\x00?\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x00\xc0\x10L\x00\x00\x1f\xff\xff\xff\xfc\x00\x00\x00\x00\x00\x03\x00\x0b#@\x00?\xff\xff\xff\xfe\x00\x00\x00\x00\x00\x1c\x16\x01 \x00\x00\x1f\xff\xff\xff\xfc\x00\x00\x00\x00\x00a\xa2\x00\x10\x00\x00\x1f\xff\xff\xff\xfe\x00\x00\x00\x00\x03\x95D\x15P\x00\x00\x1f\xff\xff\xff\xfc\x00\x00\x00\x00\x0c\x13\x05e\x0c\x00\x00?\xff\xff\xff\xfc\x00\x00\x00\x00x\xc0\xa8\xa80\x00\x00?\xff\xff\xff\xfc\x00\x00\x00\x01\x04\x00\x03)\xca\x00\x00\x7f\xff\xff\xff\xfc\x00\x00\x00\x02M\r\x12\x1c \x00\x00\xff\xff\xff\xfd\xf8\x00\x00\x00\x02\xa1 \x81\x10\xf8\x00\x03\xff\xff\xff\xfd\xf0\x00\x00\x00\x01\x15@\x83\x13\xfe\x00\x07\xff\xff\xff\xf9\xe0\x00\x00\x00\x01H\xc0\x1c\x19\xff\xd2\xaf\xff\xff\xff\xf3\xc0\x00\x00\x00\x00\x85 \xd00?\xff\xff\xff\xff\xff\xe7\x80\x00\x00\x00\x00BW\x10\xc0\x07\xff\xff\xff\xff\xff\x8e\x00\x00\x00\x00\x001\x18\x01\x00\x00\x7f\xef\xff\xff\xfc\x00\x00\x00\x00\x00\x00\t\xf0\x03\x00\x00\x01`.\xfd@\x00\x00\x00\x00\x00\x00\x05\x08\x01`\x00\x00\xc0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x03\x10\x00\x015-\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00l\x14\x00\x00\x88\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00p\n\x00\x17h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00C\x11\x80aA \x80\x00\x00\x00\x00\x00\x00\x00\x00\x008\xc0\x80\xc0\xda%\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00A\x00+\xda@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00c\x04\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00,\x08\x00\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x0c\x08\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x080\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x01\x80\n \x00\x02\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x1c@\x00\x06\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00`\x04\x80\x00\x06\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x000\x05\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x03\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)

frame_buffer_of_image = framebuf.FrameBuffer(TH3, 128, 64, framebuf.MONO_HLSB)
#oled.fill(0)
#oled.blit(frame_buffer_of_image, 0, 0)
#oled.show()
time.sleep(5)
sensor = Pin(27, Pin.IN)
# dhtsensor = dht11.DHT11(Pin(28, Pin.OUT, Pin.PULL_DOWN))
def open_eyes():
    """open eye in #oled"""
    frame_buffer_of_image = framebuf.FrameBuffer(TH, 128, 64, framebuf.MONO_HLSB)
    #oled.fill(0)
    #oled.blit(frame_buffer_of_image, 0, 0)
    #oled.show()


def close_eyes():
    """show close eyes in #oled"""
    frame_buffer_of_image = framebuf.FrameBuffer(TH2, 128, 64, framebuf.MONO_HLSB)
    #oled.fill(0)
    #oled.blit(frame_buffer_of_image, 0, 0)
    #oled.show()
    actuator_constants.led.toggle()


if __name__ == "__main__":
    movements.action_standup()
    