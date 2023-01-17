"""movements.py"""
from machine import Pin, PWM
import time
from actuator_constants import *
from message_constants import *


class MovementMechanism:
    """Movement mechanism"""

    def display_message(self, msg):
        """Display message functionality"""
        print(msg)

    def servodrive_system_with_PWM(self, pin_array, range_array, interval, mode):
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
            delta = 5000 - position
            print(position, delta)
            pwm1.duty_u16(position)
            pwm2.duty_u16(position)
            pwm3.duty_u16(5000 + delta)
            pwm4.duty_u16(5000 + delta)

        def set_servo_cycle4(position):
            delta = 5000 - position
            pwm1.duty_u16(position)
            pwm3.duty_u16(5000 + delta)

        def set_servo_cycle5(position):
            delta = 5000 - position
            pwm2.duty_u16(position)
            pwm4.duty_u16(5000 + delta)

        if mode == True:
            for pos in range(range_array[0], range_array[1], -interval):
                set_servo_cycle(pos)
                time.sleep(0.1)
            for pos in range(range_array[2], range_array[3], interval):
                set_servo_cycle2(pos)
                time.sleep(0.1)
        elif mode == False:
            for pos in range(range_array[0], range_array[1], -interval):
                print(pos)
                set_servo_cycle3(pos)
                time.sleep(0.1)

    def induvidual_servo_control(self, angle, pin_array, index):
        """Control induvidual servo actuators"""
        new_duty_cycle = MINIMUM_DUTY_CYCLE + (MAXIMUM_DUTY_CYCLE - MINIMUM_DUTY_CYCLE) * (int(angle) / 180)
        servo_pin = PWM(Pin(pin_array[index]))
        servo_pin.freq(50)
        servo_pin.duty_u16(int(new_duty_cycle))

    def action_sitdown_hard(self):
        """Action sit default hard"""
        self.display_message(SIT_DEFAULT)
        for i in LEG_SERVO_NAME:
            index_pos = LEG_SERVO_NAME.index(i)
            angle = SIT_POS[index_pos]
            new_duty_cycle = MINIMUM_DUTY_CYCLE + (MAXIMUM_DUTY_CYCLE - MINIMUM_DUTY_CYCLE) * (int(angle) / 180)
            servo_pin = PWM(Pin(LEG_SERVO_PIN[index_pos]))
            servo_pin.freq(50)
            servo_pin.duty_u16(int(new_duty_cycle))
            print("BOOMER leg " + i + " initialized ...")
            time.sleep(0.2)

    def action_transformation_sitdown_standup(self):
        """Action transformation sitdown to standup"""
        self.display_message(ACT_TXN_SIT_STAND)
        self.servodrive_system_with_PWM(
            SIT_STAND_TRANSFORMATION_PIN_ARRAY,
            SIT_STAND_TRANSFORMATION_PWM_ARRAY,
            INTERVAL,
            False,
        )

    def action_transformation_standup_to_sitdown(self):
        """Action transformation standup to sitdown"""
        self.display_message(ACT_TXN_STAND_SIT)
        self.servodrive_system_with_PWM(
            SIT_STAND_TRANSFORMATION_PIN_ARRAY,
            STAND_SIT_TRANSFORMATION_PWM_ARRAY,
            -INTERVAL,
            False,
        )

    def action_stand_hard(self):
        """Action stand default hard"""
        self.display_message(STAND_DEFAULT)
        self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[1], FRONTAL_BLEG, 0)
        self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[1], HIND_CLEG, 0)
        self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[4], HIND_DLEG, 0)
        self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[4], FRONTAL_ALEG, 0)

    def action_transformation_stand_forward_stand(self):
        """Action transformation stand to forward and bact to stand position"""
        self.display_message(ACT_TXN_STAND_FWD)
        delta1 = 0
        for angle in range(FORWARD_TRANSFORMATION_ARRAY[1], FORWARD_TRANSFORMATION_ARRAY[2]):
            delta1 = delta1 + 1
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[1] - delta1, FRONTAL_BLEG, 0)
            self.induvidual_servo_control(angle, HIND_CLEG, 0)
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[4], HIND_DLEG, 0)
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[4], FRONTAL_ALEG, 0)
            time.sleep(0.1)
        delta2 = 0
        for angle in range(FORWARD_TRANSFORMATION_ARRAY[4], FORWARD_TRANSFORMATION_ARRAY[5]):
            delta2 = delta2 + 1
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[1] - delta1, FRONTAL_BLEG, 0)
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[2], HIND_CLEG, 0)
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[4] - delta2, HIND_DLEG, 0)
            self.induvidual_servo_control(angle, FRONTAL_ALEG, 0)
            time.sleep(0.1)
        change = 0
        while change < 10:
            change = change + 1
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[0] + change, FRONTAL_BLEG, 0)
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[2] - change, HIND_CLEG, 0)
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[3] + change, HIND_DLEG, 0)
            self.induvidual_servo_control(FORWARD_TRANSFORMATION_ARRAY[5] - change, FRONTAL_ALEG, 0)
            time.sleep(0.1)

    def action_transformation_all_arms_up_down(self, IsUp):
        """Action transformation all arms up and down"""
        self.display_message(ACT_TXN_ARMS)
        delta = 0
        if IsUp == True:
            while delta < 60:
                delta = delta + 1
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[1] - delta, FRONTAL_BLEG, 2)
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[1] + delta, HIND_CLEG, 2)
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[1] - delta, HIND_DLEG, 2)
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[1] + delta, FRONTAL_ALEG, 2)
                time.sleep(0.1)
            delta = 0
        else:
            while delta < 60:
                delta = delta + 1
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[0] + delta, FRONTAL_BLEG, 2)
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[2] - delta, HIND_CLEG, 2)
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[0] + delta, HIND_DLEG, 2)
                self.induvidual_servo_control(ALL_ARMS_TRANSFORMATION_ARRAY[2] - delta, FRONTAL_ALEG, 2)
                time.sleep(0.1)
            delta = 0
