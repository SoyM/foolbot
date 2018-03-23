import time
import paho.mqtt.client as mqtt
import json

HOST = "m13.cloudmqtt.com"
PORT = 15873
USER = "lytlmnde"
PASSWORD = "3mtD81MmaVqW"


class MqttController:
    def __init__(self):
        client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.client = mqtt.Client(client_id)

    def client_loop(self):
        self.client.username_pw_set(USER, PASSWORD)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(HOST, PORT)
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("test")
        client.subscribe("admin")
        client.subscribe("servoAin")
        client.publish("test", json.dumps({"user": USER, "say": "Hello,anyone!"}))

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + msg.payload.decode("utf-8"))

    def send_message(self, message):
        self.client.publish("test", json.dumps({"user": USER, "say": message}))
