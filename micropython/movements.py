from machine import Pin,PWM
import Actuator
import Buzzer,time
def servo(degrees,name):
    try:
        if int(degrees) > 180: degrees=180
        if int(degrees) < 0: degrees=0
        maxDuty=9000
        minDuty=1000
        newDuty=minDuty+(maxDuty-minDuty)*(int(degrees)/180)
        
        if name in Actuator.legServoName:
            index_pos=Actuator.legServoName.index(name)
            Actuator.legAngle[index_pos]=degrees
        print(Actuator.legAngle)
        print("Servo Leg is:",Actuator.legServo[index_pos])
        print("Duty Cycle is:",newDuty)
        servoPin = PWM(Pin(Actuator.legServo[index_pos]))
        servoPin.freq(50)
        servoPin.duty_u16(int(newDuty))
    except:
        print("[INVALID MESSAGE FORMAT]")

def standup():
    
    for i in Actuator.legServoName:
        index_pos=Actuator.legServoName.index(i)
        angle=Actuator.legAngle[index_pos]
        maxDuty=9000
        minDuty=1000
        newDuty=minDuty+(maxDuty-minDuty)*(int(angle)/180)
        servoPin = PWM(Pin(Actuator.legServo[index_pos]))
        servoPin.freq(50)
        servoPin.duty_u16(int(newDuty))
        print("Boomer leg "+i+" initialized ...")
        time.sleep(0.2)
    Buzzer.quiet()

def Pushup():
    pwm = PWM(Pin(4))
    pwm2 = PWM(Pin(12)) 
    pwm.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position)
        time.sleep(0.01)
    for pos in range(3000,9000,50):
        setServoCycle(pos)
    for pos in range(9000,3000,-50):
        setServoCycle(pos)
        
def sleep():
    pwm = PWM(Pin(4))
    pwm2 = PWM(Pin(12)) 
    pwm.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position)
        time.sleep(0.01)
    for pos in range(3000,9000,50):
        setServoCycle(pos)
    


def Threat():
    pwm = PWM(Pin(2))
    pwm2 = PWM(Pin(10)) 
    pwm3 = PWM(Pin(5))
    pwm4 = PWM(Pin(13))
    pwm.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position)
        pwm3.duty_u16(position)
        pwm4.duty_u16(position)
        
        time.sleep(0.01)
    count=0
    while count<=10:
        count=count+1
        for pos in range(4000,6000,50):
            setServoCycle(pos)
            time.sleep(0.1)
        for pos in range(6000,4000,-50):
            setServoCycle(pos)
            time.sleep(0.1)
        for pos in range(4000,6000,50):
            setServoCycle(pos)
            time.sleep(0.1)
        for pos in range(6000,4000,-50):
            setServoCycle(pos)
            time.sleep(0.1)
   
def forward():
    #G
    pwm = PWM(Pin(10))
    pwm2 = PWM(Pin(12))
    pwm.freq(50)
    pwm2.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)       
        time.sleep(0.02)
    def setServoCycle2 (position):
        pwm2.duty_u16(position)       
        time.sleep(0.02)
    for pos in range(3500,6000,50):
        setServoCycle2(pos)
    for pos in range(6000,4000,-50):
        setServoCycle(pos)
    for pos in range(6000,3000,-50):
        setServoCycle2(pos)
    

    #D
    pwm = PWM(Pin(5))
   
    pwm.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)
       
        time.sleep(0.02)
    for pos in range(5000,3500,-50):
        setServoCycle(pos)
    '''for pos in range(3500,5000,50):
        setServoCycle(pos)'''

 


    #A
    pwm = PWM(Pin(2))
    pwm2 = PWM(Pin(4))
    pwm2.freq(50)
    pwm.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)
        time.sleep(0.02)
    def setServoCycle2 (position):
        pwm2.duty_u16(position)       
        time.sleep(0.02)
    for pos in range(3500,5000,50):
        setServoCycle2(pos)
    for pos in range(5000,3000,-50):
        setServoCycle(pos)    
    for pos in range(5000,3500,-50):
        setServoCycle2(pos)
    
    #J
    pwm = PWM(Pin(13))
   
    pwm.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)
       
        time.sleep(0.02)
    for pos in range(5000,4500,-50):
        setServoCycle(pos)
    for pos in range(4500,5000,50):
        setServoCycle(pos)

    pwm = PWM(Pin(10))
    pwm2 = PWM(Pin(5))
    pwm3 = PWM(Pin(2))
    pwm4= PWM(Pin(13))
   
    pwm.freq(50)
    def setServoCycle (position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position-500)
        pwm3.duty_u16(position-1000)
        pwm4.duty_u16(position)
       
        time.sleep(0.09)

   
    for pos in range(4500,6000,50):
        setServoCycle(pos)
    


    

