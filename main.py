from __future__ import division
import time
import json
import logging
import threading

from mqttController import MqttController
import middleCh
import motion
from servo import Servo


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

    middleCh._init()

    logging.basicConfig(level=logging.DEBUG)
    mo = motion.Motion(front_right_body, front_right_leg, front_left_body, front_left_leg, rear_left_body,
                       rear_left_leg,
                       rear_right_body, rear_right_leg)
    autoMove = 0

    print('Init success, press Ctrl-C to quit...')

    while True:
        ch = middleCh.get_value("bot_mode")
        mqtt.client.publish("bot_mode", json.dumps({
            "bot_mode": ch,
            "update_date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }))
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
            time.sleep(0.5)

        if autoMove:
            mo.autonomy()
