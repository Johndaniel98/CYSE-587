# MQTT Configuration and Broker Setup

This file outlines the steps to install, configure, and run the MQTT broker (Mosquitto) used in this project, including TLS setup for secure message transmission.

---

## 🧰 Tools Required

- [Mosquitto MQTT Broker](https://mosquitto.org/)
- OpenSSL (for generating certificates)
- Python 3 with `paho-mqtt` library
- Optional: A Linux terminal or Windows with WSL/PowerShell

---

## ⚙️ 1. Install Mosquitto

### On Debian/Ubuntu:
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
```

### On Windows:
- Download the installer from: https://mosquitto.org/download/
- Install and ensure `mosquitto.exe` is added to your system PATH.

---

## 🔐 2. Generate TLS Certificates (if using TLS)

You can use OpenSSL to generate a self-signed certificate:

```bash
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365
```

Place the resulting files (`ca.crt`, `server.crt`, `server.key`) in a folder, e.g., `certs/`.

---

## 📝 3. Broker Configuration (mosquitto.conf)

Create a file called `mosquitto.conf` with the following content for TLS:

```ini
listener 8883
cafile certs/ca.crt
certfile certs/server.crt
keyfile certs/server.key
require_certificate false
```

Place this config file in the project root or specify its path when running Mosquitto.

---

## 🚀 4. Run the Broker

### Basic (no TLS):
```bash
mosquitto -v
```

### With TLS:
```bash
mosquitto -c mosquitto.conf -v
```

You should see a message indicating it’s listening on port 8883.

---

## ✅ 5. Verifying the Setup

### Test Broker Connection (optional):
```bash
mosquitto_pub -h localhost -t "test/topic" -m "Hello"
mosquitto_sub -h localhost -t "test/topic"
```

### Python TLS Example:
Ensure the Python client uses:
```python
client.tls_set("path/to/ca.crt")
client.connect("localhost", 8883)
```

Refer to `publishertls.py` and `subscribertls.py` in this repo for working examples.

---

## 🧾 Notes

- Make sure your firewall allows port 8883.
- Certificates must match paths defined in both `mosquitto.conf` and your Python code.
- For testing, self-signed certificates are fine, but production systems require certificates from a trusted CA.
