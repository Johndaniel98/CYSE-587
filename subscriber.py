# subscriber.py
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPIC = "victim/+/#"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print(f"[{msg.topic}] → {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_forever()
