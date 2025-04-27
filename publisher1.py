import uuid, json, time
from paho.mqtt import client as mqtt

# Generate one token per run
CLIENT_TOKEN = uuid.uuid4().hex

def on_connect(client, userdata, flags, rc):
    print(f"Connected with pseudonym {CLIENT_TOKEN}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883)    # or your broker address
client.loop_start()

def publish_reading(data):
    payload = {
        "id": CLIENT_TOKEN,
        "timestamp": time.time(),
        "data": data
    }
    client.publish("calamity/messages", json.dumps(payload))

# Example usage:
if __name__ == "__main__":
    for reading in [23.4, 24.1, 22.8]:
        publish_reading(reading)
        time.sleep(1)
