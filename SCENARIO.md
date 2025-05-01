# SCENARIO.md – System Test Description

## Scenario

This project simulates an MQTT-based disaster response system, where victim devices send distress messages to a drone-based MQTT broker, which forwards them to a C2 system for coordination.

Two implementations are tested:

1. **Without Privacy Enhancements (Plain MQTT):**
   - Victim ID and full coordinates are visible.
   - Messages are transmitted in plaintext over port 1883.

2. **With Privacy Enhancements (PETs - TLS + Pseudonymization):**
   - Victim IDs replaced by pseudonyms (UUID).
   - Messages encrypted using TLS on port 8883.
   - Topics are generic and unlinkable (`calamity/messages`).

---

## Setup

1. Install Mosquitto broker and Python dependencies:
```bash
pip install paho-mqtt
```

2. Run broker in plaintext mode for the first test (`port 1883`).

3. Enable TLS with certificates (`port 8883`) for secure mode.

---

## Run Instructions

### Plain MQTT (Without PETs)
```bash
python subscriber.py
python publisher.py
```

### TLS + PETs (Encrypted and Pseudonymized)
```bash
python subscribertls.py
python publishertls.py
```

---

## Sample Messages

### Plain MQTT
```json
{
  "casualty_id": "V001",
  "event_time": "2025-04-30T14:00:00Z",
  "coordinates": {
    "lat": 38.8372,
    "lon": -77.2996
  },
  "status": "distress"
}
```

### With PETs (TLS + UUID)
```json
{
  "pseudoid": "e3b0c44298fc1c149afbf4c8996fb924",
  "event_time": "2025-04-30T14:00:00Z",
  "coordinates": {
    "latitude": 38.8372,
    "longitude": -77.2996
  },
  "status": "distress"
}
```

---

## Expected Results

| Configuration          | Outcome                                                |
|------------------------|--------------------------------------------------------|
| Plain MQTT             | Data and metadata (IDs, GPS) visible; high privacy risk |
| TLS + PETs             | Data encrypted; IDs pseudonymized; improved privacy    |

See `Part 4.pdf` for a detailed comparison and risk evaluation metrics.
