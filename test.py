import requests
import time
from mqttController import MqttController
import threading
import json
import middleCh

# while True:
#     r = requests.get('http://111.230.224.190/get_set_motion/')
#
#     ch = r.json()['set_mode']
#     payload = {'bot_mode': ch}
#     print(ch)
#     r = requests.post('http://111.230.224.190/update_bot_motion/', json=payload)
#     print(r.text)
#     time.sleep(1)
mqtt = MqttController()

t1 = threading.Thread(target=mqtt.client_loop)
t1.setDaemon(True)
t1.start()

middleCh.init()

while True:
    ch = middleCh.get_value("bot_mode")
    mqtt.client.publish("bot_mode", json.dumps({
        "bot_mode": ch,
        "update_date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }))
    time.sleep(0.7)
