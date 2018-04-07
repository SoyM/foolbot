from communications.mqttController import MqttController
import threading

mq = MqttController()
t1 = threading.Thread(target=mq.client_loop)
t1.setDaemon(True)
t1.start()

while 1:
    mq.send_message(input())
