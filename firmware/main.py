"""main.py"""
from machine import Pin, UART, PWM, I2C
from ssd1306 import SSD1306_I2C
import time
class BootSystem:
    """Boot System Main Controller"""

    def set_normal_boot(self):
        """import normal boot"""
        import normal_boot
        del normal_boot

    def set_safe_boot(self):
        """import safe boot"""        
        import safe_boot

    def initialize_boot(self):
        try:            
            i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
            oled = SSD1306_I2C(128, 64, i2c)
            oled.fill(0)
            print("Normal Booting...")
            self.set_normal_boot()
        except:            
            print("Safe Booting ...")         
            self.set_safe_boot()

BootSystem().initialize_boot()
