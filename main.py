from __future__ import division
import time
import logging
import pca9685
import motion
import threading
from mqttController import MqttController
import json
import middleCh


class Servo:
    def __init__(self, channel):
        self.channel = channel
        self.angle = 0
        # Initialise the PCA9685 using the default address (0x40).
        # Alternatively specify a different address and/or bus:
        # pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
        self.pwm = pca9685.PCA9685()

        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(50)

        self.servo_min = 150  # Min pulse length out of 4096
        self.servo_max = 600  # Max pulse length out of 4096

    def write(self, angle):
        self.angle = angle
        self.set_servo_angle(self.channel, self.angle)
        # print("channel:{0},angle:{1}".format(self.channel, self.angle))

    def set_servo_angle(self, channel, angle):
        pulse = angle * 5
        pulse //= 2
        pulse += 150
        self.pwm.set_pwm(channel, 0, pulse)
        print(pulse)

    def move_extreme(self):
        # Move servo on channel O between extremes.
        # self.pwm.set_pwm(0, 0, self.servo_min)
        self.write(10)
        print("min")
        time.sleep(1)
        ##        self.pwm.set_pwm(1, 0, self.servo_min)
        time.sleep(1)
        ##        self.pwm.set_pwm(1, 0, self.servo_max)
        time.sleep(1)
        ##        self.pwm.set_pwm(0, 0, self.servo_max)
        self.write(170)
        time.sleep(1)

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000  # 1,000,000 us per second
        pulse_length //= 52  # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096  # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)


front_right_body = Servo(0)
front_right_leg = Servo(1)
front_left_body = Servo(2)
front_left_leg = Servo(3)
rear_left_body = Servo(4)
rear_left_leg = Servo(5)
rear_right_body = Servo(6)
rear_right_leg = Servo(7)


def setup():
    front_right_body.write(40)
    front_right_leg.write(90)
    front_left_body.write(120)
    front_left_leg.write(90)
    rear_left_body.write(40)
    rear_left_leg.write(90)
    rear_right_body.write(120)
    rear_right_leg.write(90)


if __name__ == '__main__':
    setup()
    mqtt = MqttController()
    t1 = threading.Thread(target=mqtt.client_loop)
    t1.setDaemon(True)
    t1.start()

    logging.basicConfig(level=logging.DEBUG)
    mo = motion.Motion(front_right_body, front_right_leg, front_left_body, front_left_leg, rear_left_body,
                       rear_left_leg,
                       rear_right_body, rear_right_leg)
    autoMove = 0

    print('Moving servo on channel 0, press Ctrl-C to quit...')

    while True:
        ch = middleCh.get_value("bot_mode")
        mqtt.client.publish("bot_mode", json.dumps({"bot_mode": ch}))
        if ch:
            if ch == 'up':
                mo.forward()
            if ch == 'down':
                mo.back()
            if ch == 'right':
                mo.right()
            if ch == 'left':
                mo.left()
            if ch == 'wave':
                mo.wave()
                mo.stand()
                mo.wave2()
                mo.stand()
            if ch == 'sleep':
                mo.sleep()
            if ch == 'stand':
                mo.stand()

            # Pressing a once causes the robot to begin moving autonomously,
            #  and pressing it again causes the robot to stop
            if ch == 'auto':
                if autoMove == 0:
                    autoMove = 1
            else:
                autoMove = 0
        else:
            time.sleep(1)

        if autoMove:
            mo.autonomy()
