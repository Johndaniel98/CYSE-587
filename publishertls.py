import uuid, json, time, ssl
from paho.mqtt import client as mqtt

# 1. Generate a token for this session
CLIENT_TOKEN = uuid.uuid4().hex

# 2. MQTT setup
client = mqtt.Client()
client.tls_set(
    ca_certs="C:/mosquitto/certs/ca.crt",
    tls_version=ssl.PROTOCOL_TLSv1_2
)
client.on_connect = lambda c, u, f, rc: print(f"Connected with token {CLIENT_TOKEN} (rc={rc})")
client.connect("localhost", 8883)
client.loop_start()

# 3. Publish a few readings
def publish_reading(sensor_data):
    payload = {
        "id": CLIENT_TOKEN,
        "timestamp": time.time(),
        "data": sensor_data
    }
    client.publish("calamity/messages", json.dumps(payload))
    print("Published:", payload)

if __name__ == "__main__":
    for reading in [23.4, 24.1, 22.8]:
        publish_reading(reading)
        time.sleep(1)
    client.loop_stop()
    client.disconnect()
