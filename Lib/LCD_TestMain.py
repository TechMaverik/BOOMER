from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
    print(I2C_ADDR)
    lcd.blink_cursor_on()
    lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
    lcd.putstr("Sasappa")
    sleep(2)
    lcd.clear()
    lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
    lcd.putstr("Moomoo")
    sleep(2)
    lcd.blink_cursor_off()
    lcd.clear()
    lcd.putstr("SASAPPA LOVES   ")
    lcd.putstr("MOOMOO   ")
    
    
    #0x00,0x00,0x1B,0x1F,0x0E,0x04,0x00,0x00
    for i in range(10):
        lcd.backlight_on()
        sleep(0.2)
        lcd.backlight_off()
        sleep(0.2)
    lcd.backlight_on()
    lcd.hide_cursor()
    lcd.clear()
