from time import sleep
from machine import Pin
from machine import PWM
pwm = PWM(Pin(12))
pwm1 = PWM(Pin(10))
pwm.freq(50)
#Function to set an angle
#The position is expected as a parameter
def setServoCycle (position):
    pwm.duty_u16(position)
    #pwm1.duty_u16(position)
    sleep(0.01)
while True:
    for pos in range(7000,9000,50):
        setServoCycle(pos)
    for pos in range(9000,7000,-50):
        setServoCycle(pos)
