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
        elif mode == "F1":
            for pos in range(range_array[0], range_array[1], interval):
                set_servo_cycle4(pos)
                time.sleep(0.1)
            for pos in range(range_array[2], range_array[3], -interval):
                set_servo_cycle5(pos)
                time.sleep(0.1)
        elif mode == "F2":
            for pos in range(range_array[2], range_array[3], -interval):
                set_servo_cycle5(pos)
                time.sleep(0.1)
            for pos in range(range_array[0], range_array[1], interval):
                set_servo_cycle4(pos)
                time.sleep(0.1)

    def induvidual_servo_control(self, angle, pin_array, index):
        """Control induvidual servo actuators"""
        new_duty_cycle = MINIMUM_DUTY_CYCLE + (
            MAXIMUM_DUTY_CYCLE - MINIMUM_DUTY_CYCLE
        ) * (int(angle) / 180)
        servo_pin = PWM(Pin(pin_array[index]))
        servo_pin.freq(50)
        servo_pin.duty_u16(int(new_duty_cycle))
        # print("GIVEN " + str(pin_array[index]) + " " + str(angle))

    def action_sitdown(self):
        """Arranging legs to sit position"""
        for i in LEG_SERVO_NAME:
            index_pos = LEG_SERVO_NAME.index(i)
            angle = SIT_POS[index_pos]
            new_duty_cycle = MINIMUM_DUTY_CYCLE + (
                MAXIMUM_DUTY_CYCLE - MINIMUM_DUTY_CYCLE
            ) * (int(angle) / 180)
            servo_pin = PWM(Pin(LEG_SERVO_PIN[index_pos]))
            servo_pin.freq(50)
            servo_pin.duty_u16(int(new_duty_cycle))
            print("Boomer leg " + i + " initialized ...")
            time.sleep(0.2)

    def action_transformation_standup_forward(self):
        """Action transformation stand to forward"""
        print("Action transformation stand to forward")
        self.servodrive_system(
            STAND_FORWARD_TRANSFORMATION_PIN_ARRAY,
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY,
            INTERVAL,
            "F1",
        )

    def action_transformation_forward_standup(self):
        """Action transformation stand to forward"""
        print("Action transformation stand to forward")
        self.servodrive_system(
            STAND_FORWARD_TRANSFORMATION_PIN_ARRAY,
            FORWARD_STAND_TRANSFORMATION_PWM_ARRAY,
            INTERVAL,
            "F2",
        )

    def action_transformation_standup_forward_all(self):
        """Action transformation stand to forward"""
        print("Action transformation stand to forward all")
        self.servodrive_system(
            STAND_FORWARD_TRANSFORMATION_PIN_ARRAY,
            FORWARD_STAND_TRANSFORMATION_PWM_ARRAY,
            -INTERVAL,
            False,
        )

    def action_transformation_sitdown_standup(self):
        """Action transformation sitdown to standup"""
        print("Action transformation sitdown to standup")
        self.servodrive_system(
            SIT_STAND_TRANSFORMATION_PIN_ARRAY,
            SIT_STAND_TRANSFORMATION_PWM_ARRAY,
            INTERVAL,
            False,
        )

    def action_transformation_standup_to_sitdown(self):
        """Action transformation standup to sitdown"""
        print("Action transformation standup to sitdown")
        self.servodrive_system(
            SIT_STAND_TRANSFORMATION_PIN_ARRAY,
            STAND_SIT_TRANSFORMATION_PWM_ARRAY,
            -INTERVAL,
            False,
        )

    def action_transformation_standup_move_forward_step(self):
        """Action transformation standup and move forward in step"""
        # B Frontal Arm
        shoulder = PWM(Pin(FRONTAL_BLEG[0]))
        mid_arm = PWM(Pin(FRONTAL_BLEG[1]))
        arm = PWM(Pin(FRONTAL_BLEG[2]))

        def servo_movement_control(position):
            shoulder.duty_u16(position)

        for pos in range(
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[2],
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[3],
            -50,
        ):
            self.induvidual_servo_control(30, FRONTAL_BLEG, 2)
            servo_movement_control(pos)
            time.sleep(0.1)
            self.induvidual_servo_control(90, FRONTAL_BLEG, 2)

        # C Hind Arm
        shoulder = PWM(Pin(HIND_CLEG[0]))
        mid_arm = PWM(Pin(HIND_CLEG[1]))
        arm = PWM(Pin(HIND_CLEG[2]))

        for pos in range(
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[0],
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[1],
            50,
        ):
            # self.induvidual_servo_control(150, HIND_CLEG, 2)
            servo_movement_control(pos)
            time.sleep(0.1)
            # self.induvidual_servo_control(90, HIND_CLEG, 2)

        # D Hind Arm
        print("d hinmd leg")
        shoulder = PWM(Pin(HIND_DLEG[0]))
        mid_arm = PWM(Pin(HIND_DLEG[1]))
        arm = PWM(Pin(HIND_DLEG[2]))

        for pos in range(
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[2],
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[3],
            -50,
        ):
            # self.induvidual_servo_control(30, HIND_DLEG, 2)
            servo_movement_control(pos)
            time.sleep(0.1)
            # self.induvidual_servo_control(90, HIND_DLEG, 2)

        # A Front Arm
        shoulder = PWM(Pin(FRONTAL_ALEG[0]))
        mid_arm = PWM(Pin(FRONTAL_ALEG[1]))
        arm = PWM(Pin(FRONTAL_ALEG[2]))

        for pos in range(
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[0],
            STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[1],
            50,
        ):
            # self.induvidual_servo_control(150, FRONTAL_ALEG, 2)
            servo_movement_control(pos)
            time.sleep(0.1)
            # self.induvidual_servo_control(90, FRONTAL_ALEG, 2)

        # shouldera = PWM(Pin(FRONTAL_BLEG[0]))
        # shoulderb = PWM(Pin(HIND_CLEG[0]))
        # shoulderc = PWM(Pin(HIND_DLEG[0]))
        # shoulderd = PWM(Pin(FRONTAL_ALEG[0]))

        # def servo_movement_control_all(position):
        #     print(position)
        #     error = 5000 - position
        #     shouldera.duty_u16(position)
        #     # shoulderb.duty_u16(5000 + error)
        #     shoulderc.duty_u16(position)
        #     # shoulderd.duty_u16(5000 + error)
        #     time.sleep(0.1)

        # for pos in range(
        #     STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[0],
        #     STAND_FORWARD_TRANSFORMATION_PWM_ARRAY[1],
        #     50,
        # ):
        #     servo_movement_control_all(pos)
