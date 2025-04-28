import ssl, json
from paho.mqtt import client as mqtt

# 1. MQTT setup
client = mqtt.Client()
client.tls_set(
    ca_certs="C:/mosquitto/certs/ca.crt",
    tls_version=ssl.PROTOCOL_TLSv1_2
)
def on_connect(c, u, f, rc):
    print("Subscriber connected (rc=", rc, ")")
    c.subscribe("calamity/messages")

def on_message(c, u, msg):
    data = json.loads(msg.payload)
    print("Received pseudonymized message:", data)

client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 8883)
client.loop_forever()
