# publisher.py
import json
import time
import paho.mqtt.client as mqtt

BROKER = "localhost"
VICTIM_ID = "V001"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

for i in range(5):
    msg = {
        "victim_id": VICTIM_ID,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "location": {"lat": 38.8372 + 0.001*i, "lon": -77.2996 - 0.001*i},
        "status": "distress"
    }
    topic = f"victim/{VICTIM_ID}/status"
    client.publish(topic, json.dumps(msg))
    print(f"Published to {topic}: {msg}")
    time.sleep(2)
