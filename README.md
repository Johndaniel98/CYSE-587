# Calamity MQTT Privacy Project

## Overview
This project simulates a secure MQTT-based communication system during a calamity scenario. Victim devices publish distress messages to a broker (drone), and a C2 system subscribes to these messages. Privacy-enhancing technologies are implemented using TLS encryption and pseudonymization.

## Tools Used
- **Python 3**
- **paho-mqtt** (Python MQTT client)
- **Mosquitto** (MQTT broker)
- **OpenSSL** for generating TLS certificates

## Installation

### 1. Install Dependencies

```bash
pip install paho-mqtt
```

### 2. Setup Mosquitto Broker

Download and install Mosquitto from: [https://mosquitto.org/download](https://mosquitto.org/download)

Make sure it's configured with TLS support. Example certs are expected at:
```
C:/mosquitto/certs/ca.crt
```

To run the broker with TLS:
```bash
mosquitto -c mosquitto.conf -v
```

### 3. Run the Code

#### Without TLS (Baseline)
```bash
python publisher.py
python subscriber.py
```

#### With TLS and PETs (Encrypted + Pseudonymized)
```bash
python publishertls.py
python subscribertls.py
```

## Project Structure

| File              | Purpose                                      |
|-------------------|----------------------------------------------|
| `publisher.py`    | Plaintext MQTT publisher                     |
| `subscriber.py`   | Plaintext MQTT subscriber                    |
| `publishertls.py` | TLS-enabled, pseudonymized publisher         |
| `subscribertls.py`| TLS-enabled subscriber                       |
| `Part 4.pdf`      | Evaluation and metrics                       |
| `new_model-1.pdf` | LINDDUN privacy threat model                 |
| `Problem Description.pdf` | Project requirement specification   |
