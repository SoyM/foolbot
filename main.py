from __future__ import division
import time
import logging
import paho.mqtt.client as mqtt
import pca9685
import motion
import threading


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
        self.pwm.set_pwm(self.channel, 0, angle)
        print(self.angle)

    def attach(self, channel):
        self.channel = channel

    def set_servo_angle(self, channel, angle):
        pulse = angle * 5
        pulse //= 2 + 150
        self.pwm.set_pwm(channel, 0, pulse)

    def move_extreme(self):
        # Move servo on channel O between extremes.
        self.pwm.set_pwm(0, 0, self.servo_min)
        print("min")
        time.sleep(1)
        self.pwm.set_pwm(1, 0, self.servo_min)
        time.sleep(1)
        self.pwm.set_pwm(1, 0, self.servo_max)
        time.sleep(1)
        self.pwm.set_pwm(0, 0, self.servo_max)
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

HOST = "m13.cloudmqtt.com"
PORT = 15873


def setup():
    front_right_body.attach(6)
    front_right_body.write(40)
    front_right_leg.attach(7)
    front_right_leg.write(90)
    front_left_body.attach(8)
    front_left_body.write(120)
    front_left_leg.attach(9)
    front_left_leg.write(90)
    rear_left_body.attach(10)
    rear_left_body.write(40)
    rear_left_leg.attach(11)
    rear_left_leg.write(90)
    rear_right_body.attach(4)
    rear_right_body.write(120)
    rear_right_leg.attach(5)
    rear_right_leg.write(90)


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    client = mqtt.Client(client_id)
    client.username_pw_set("lytlmnde", "3mtD81MmaVqW")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT)
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test")
    client.subscribe("admin")
    client.subscribe("servoAin")


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("utf-8"))


if __name__ == '__main__':
    setup()
    t1 = threading.Thread(target=client_loop)
    t1.setDaemon(True)
    t1.start()
    logging.basicConfig(level=logging.DEBUG)
    mo = motion.Motion(front_right_body, front_right_leg, front_left_body, front_left_leg, rear_left_body,
                       rear_left_leg,
                       rear_right_body, rear_right_leg)

    autoMove = 1

    print('Moving servo on channel 0, press Ctrl-C to quit...')
    while True:
        if 1:
            ch = "f"
            if ch == 'f':
                mo.forward()
            if ch == 'b':
                mo.back()
            if ch == 'r':
                mo.right()
            if ch == 'l':
                mo.left()
            if ch == 'w':
                mo.wave()
                mo.stand()
                mo.wave2()
                mo.stand()
            if ch == 's':
                mo.sleep()
            if ch == 'u':
                mo.stand()

            # Pressing a once causes the robot to begin moving autonomously,
            #  and pressing it again causes the robot to stop
            if ch == 'a':
                if ~autoMove:
                    waveCount2 = 0
                    autoMove = 1
            else:
                autoMove = 0

        if autoMove:
            mo.autonomy()
