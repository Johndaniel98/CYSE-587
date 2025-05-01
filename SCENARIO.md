# SCENARIO.md – System Test Description

## Scenario

- Victim devices send GPS and status data via MQTT to a centralized broker.
- The broker forwards these messages to the C2 (subscriber) system.
- Initially, messages are unprotected. Later, TLS and pseudonymization are added.

## Setup

1. Run Mosquitto with default config (`port 1883`) for the initial system.
2. Then enable TLS with certificates on `port 8883`.
3. Observe traffic via MQTT messages on both configurations.

## Messages

Example message (Plain):
```json
{
  "casualty_id": "V001",
  "event_time": "2025-04-30T14:00:00Z",
  "coordinates": {"lat": 38.8372, "lon": -77.2996},
  "status": "distress"
}
```

Example message (With PETs):
```json
{
  "pseudoid": "c2f7a8ab35d94e6db3a0b0e267fd754c",
  "event_time": "2025-04-30T14:00:00Z",
  "coordinates": {"latitude": 38.8372, "longitude": -77.2996},
  "status": "distress"
}
```

## Expected Results

| Test Case                  | Outcome                                                 |
|----------------------------|---------------------------------------------------------|
| Plain MQTT                 | Messages are visible in cleartext; IDs easily linkable  |
| TLS + Pseudonymization     | Encrypted traffic, pseudonymized IDs, unlinkable topics |

See `Part 4.pdf` for full risk score metrics and evaluations.
