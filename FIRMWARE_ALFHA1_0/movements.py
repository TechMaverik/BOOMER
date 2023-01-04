"""movements.py"""
from machine import Pin, PWM
import time
from actuator_constants import *


class MovementMechanism:
    """Movement mechanism"""

    def servodrive_system(self, pin_array, range_array, interval, mode):
        """Servodrive_system"""
        pwm1 = PWM(Pin(pin_array[0]))
        pwm2 = PWM(Pin(pin_array[1]))
        pwm3 = PWM(Pin(pin_array[2]))
        pwm4 = PWM(Pin(pin_array[3]))

        def set_servo_cycle(position):
            pwm1.duty_u16(position)
            pwm2.duty_u16(position)
            time.sleep(0.01)

        def set_servo_cycle2(position):
            pwm3.duty_u16(position)
            pwm4.duty_u16(position)
            time.sleep(0.01)

        def set_servo_cycle3(position):
            pwm1.duty_u16(position)
            pwm2.duty_u16(position)
            pwm3.duty_u16(position)
            pwm4.duty_u16(position)

        if mode == True:
            for pos in range(range_array[0], range_array[1], interval):
                set_servo_cycle(pos)
                time.sleep(0.1)
            for pos in range(range_array[2], range_array[3], -interval):
                set_servo_cycle2(pos)
                time.sleep(0.1)
        elif mode == False:
            for pos in range(range_array[0], range_array[1], interval):
                set_servo_cycle3(pos)
                time.sleep(0.1)

    def action_sitdown(self):
        """Arranging legs to sit position"""
        for i in LEG_SERVO_NAME:
            index_pos = LEG_SERVO_NAME.index(i)
            angle = SIT_POS[index_pos]
            max_duty_cycle = 9000
            min_duty_cycle = 1000
            new_duty_cycle = min_duty_cycle + (max_duty_cycle - min_duty_cycle) * (
                int(angle) / 180
            )
            servo_pin = PWM(Pin(LEG_SERVO_PIN[index_pos]))
            servo_pin.freq(50)
            servo_pin.duty_u16(int(new_duty_cycle))
            print("Boomer leg " + i + " initialized ...")
            time.sleep(0.2)

    def action_transformation_sitdown_standup(self):
        """Action transformation sitdown to standup"""
        self.servodrive_system(
            SIT_STAND_TRANSFORMATION_PIN_ARRAY,
            SIT_STAND_TRANSFORMATION_PWM_ARRAY,
            INTERVAL,
            True,
        )

    def action_transformation_standup_to_sitdown(self):
        """Action transformation standup to sitdown"""
        self.servodrive_system(
            SIT_STAND_TRANSFORMATION_PIN_ARRAY,
            STAND_SIT_TRANSFORMATION_PWM_ARRAY,
            -INTERVAL,
            True,
        )
