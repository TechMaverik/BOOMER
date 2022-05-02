from machine import Pin
import time
sensor=Pin(27,Pin.IN)

while True:
    print(sensor.value())
    time.sleep(1)