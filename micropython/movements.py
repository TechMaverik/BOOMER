from machine import Pin, PWM
import micropython.actuator_constants as actuator_constants
import micropython.buzzer_music_controls as buzzer_music_controls, time


def servo(degrees, name):
    """select servo and control it"""
    try:
        if int(degrees) > 180:
            degrees = 180
        if int(degrees) < 0:
            degrees = 0
        max_duty_cycle = 9000
        min_duty_cycle = 1000
        new_duty_cycle = min_duty_cycle + (max_duty_cycle - min_duty_cycle) * (int(degrees) / 180)

        if name in actuator_constants.legServoName:
            index_pos = actuator_constants.legServoName.index(name)
            actuator_constants.legAngle[index_pos] = degrees
        print(actuator_constants.legAngle)
        print("Servo Leg is:", actuator_constants.legServo[index_pos])
        print("Duty Cycle is:", new_duty_cycle)
        servo_pin = PWM(Pin(actuator_constants.legServo[index_pos]))
        servo_pin.freq(50)
        servo_pin.duty_u16(int(new_duty_cycle))
    except:
        print("[INVALID MESSAGE FORMAT]")


def action_standup():
    """arranging legs in stand position"""
    for i in actuator_constants.legServoName:
        index_pos = actuator_constants.legServoName.index(i)
        angle = actuator_constants.legAngle[index_pos]
        max_duty_cycle = 9000
        min_duty_cycle = 1000
        new_duty_cycle = min_duty_cycle + (max_duty_cycle - min_duty_cycle) * (int(angle) / 180)
        servo_pin = PWM(Pin(actuator_constants.legServo[index_pos]))
        servo_pin.freq(50)
        servo_pin.duty_u16(int(new_duty_cycle))
        print("Boomer leg " + i + " initialized ...")
        time.sleep(0.2)
    buzzer_music_controls.quiet()


def action_push_up():
    """function for making the robot to do push up"""
    pwm = PWM(Pin(4))
    pwm2 = PWM(Pin(12))
    pwm.freq(50)

    def set_servo_cycle(position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position)
        time.sleep(0.01)

    for pos in range(3000, 9000, 50):
        set_servo_cycle(pos)
    for pos in range(9000, 3000, -50):
        set_servo_cycle(pos)


def sleep():
    """function to set sleep count"""
    pwm = PWM(Pin(4))
    pwm2 = PWM(Pin(12))
    pwm.freq(50)

    def set_servo_cycle(position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position)
        time.sleep(0.01)

    for pos in range(3000, 9000, 50):
        set_servo_cycle(pos)


def action_wiggle():
    """function to set up wiggling motion"""
    pwm = PWM(Pin(2))
    pwm2 = PWM(Pin(10))
    pwm3 = PWM(Pin(5))
    pwm4 = PWM(Pin(13))
    pwm.freq(50)

    def set_servo_cycle(position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position)
        pwm3.duty_u16(position)
        pwm4.duty_u16(position)

        time.sleep(0.01)

    count = 0
    while count <= 10:
        count = count + 1
        for pos in range(4000, 6000, 50):
            set_servo_cycle(pos)
            time.sleep(0.1)
        for pos in range(6000, 4000, -50):
            set_servo_cycle(pos)
            time.sleep(0.1)
        for pos in range(4000, 6000, 50):
            set_servo_cycle(pos)
            time.sleep(0.1)
        for pos in range(6000, 4000, -50):
            set_servo_cycle(pos)
            time.sleep(0.1)


def action_forward():
    """function to set up action formward movement"""
    # G
    pwm = PWM(Pin(10))
    pwm2 = PWM(Pin(12))
    pwm.freq(50)
    pwm2.freq(50)

    def set_servo_cycle(position):
        pwm.duty_u16(position)
        time.sleep(0.02)

    def set_servo_cycle2(position):
        pwm2.duty_u16(position)
        time.sleep(0.02)

    for pos in range(3500, 6000, 50):
        set_servo_cycle2(pos)
    for pos in range(6000, 4000, -50):
        set_servo_cycle(pos)
    for pos in range(6000, 3000, -50):
        set_servo_cycle2(pos)

    # D
    pwm = PWM(Pin(5))

    pwm.freq(50)
    for pos in range(5000, 3500, -50):
        set_servo_cycle(pos)

    # A
    pwm = PWM(Pin(2))
    pwm2 = PWM(Pin(4))
    pwm2.freq(50)
    pwm.freq(50)

    for pos in range(3500, 5000, 50):
        set_servo_cycle2(pos)
    for pos in range(5000, 3000, -50):
        set_servo_cycle(pos)
    for pos in range(5000, 3500, -50):
        set_servo_cycle2(pos)

    # J
    pwm = PWM(Pin(13))

    pwm.freq(50)

    for pos in range(5000, 4500, -50):
        set_servo_cycle(pos)
    for pos in range(4500, 5000, 50):
        set_servo_cycle(pos)

    pwm = PWM(Pin(10))
    pwm2 = PWM(Pin(5))
    pwm3 = PWM(Pin(2))
    pwm4 = PWM(Pin(13))

    pwm.freq(50)

    def set_servo_cycle_3(position):
        pwm.duty_u16(position)
        pwm2.duty_u16(position - 500)
        pwm3.duty_u16(position - 1000)
        pwm4.duty_u16(position)

        time.sleep(0.09)

    for pos in range(4500, 6000, 50):
        set_servo_cycle_3(pos)
