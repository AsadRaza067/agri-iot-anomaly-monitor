# Decentralised Anomaly Detection in Heterogeneous Agri-IoT Networks Using Edge Computing

A real-time IoT sensor monitoring and anomaly detection dashboard for Agri-food supply chains detecting environmental breaches and cyber anomalies across distributed edge nodes.

## The Problem

Agri-food supply chains are uniquely vulnerable. A single undetected temperature breach in cold storage can spoil an entire shipment. A humidity anomaly in a processing zone can trigger product contamination. And increasingly, these same IoT sensor networks are targets for cyberattacks where a manipulated sensor reading looks identical to a genuine equipment fault.

Most small and mid-scale agri-food operations have no real-time visibility into what their IoT nodes are reporting. Anomalies go undetected for minutes or hours. By the time an alert is raised, the damage is done.

This project was built to address that gap a lightweight, edge-deployable anomaly detection dashboard that monitors heterogeneous IoT nodes in real time, classifies breaches by severity, and logs every event with a timestamp for audit and response.

---

## Project Overview

This system simulates a decentralised IoT monitoring setup across four Agri-food supply chain nodes.

### The system:

- Ingests real-time sensor data from multiple heterogeneous nodes (cold storage, warehouses, transport units, processing zones)
- Detects anomalies using rule-based threshold logic across temperature, humidity, and CO₂ streams
- Classifies every breach as **CRITICAL** or **WARNING** for immediate operational awareness
- Displays a live dashboard with alert logging, historical trend charts, and anomaly statistics
- Auto-refreshes every 5 seconds for continuous monitoring

---

## Monitored Nodes

| Node | Supply Chain Stage | Monitored Process |
|--------|-------------------|------------------|
| Cold Storage Unit | Warehouse Storage | Cold chain preservation and ambient climate control |
| Processing Zone | Primary Processing | Environmental monitoring during active processing |
| Transport Unit | Logistics & Distribution | In-transit mobile sensor telemetry |
| Distribution Hub | Retail Logistics | Final-mile inventory reception and dispatch |

---

## Sensor Streams & Threshold Boundaries

| Sensor | Safe Zone | Risk |
|----------|----------|------|
| Temperature | 1°C – 8°C | Cold chain breach → product spoilage |
| Humidity | 55% – 85% | Environmental degradation → contamination risk |
| CO₂ Level | Normal operating range | Atmospheric anomaly → storage integrity risk |

---

## Tech Stack

| Layer | Technology |
|---------|-----------|
| Backend | Python, Flask |
| Anomaly Detection | Rule-based threshold logic (extensible to ML) |
| Frontend Dashboard | HTML, CSS, JavaScript, Chart.js |
| Data Simulation | Python sensor models with randomised walk variants |

---

## Features

- Live sensor readings from all four simulated nodes
- Real-time anomaly detection with CRITICAL and WARNING alerts
- Historical trend visualisation using Chart.js
- Timestamped alert logging with exact breach values
- Statistics panel showing total readings, anomaly count, and anomaly rate
- Automatic dashboard refresh every 5 seconds

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/AsadRaza067/Decentralised-Anomaly-Detection-in-Heterogeneous-Agri-IoT-Networks-Using-Edge-Computing

# 2. Enter the project directory
cd Decentralised-Anomaly-Detection-in-Heterogeneous-Agri-IoT-Networks-Using-Edge-Computing

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open your browser
http://localhost:5000
```

---

## Project Structure

```text
agri-iot-anomaly-monitor/
│
├── app.py                  # Flask backend — sensor simulation + anomaly detection engine
├── requirements.txt        # Python dependencies
├── index.html              # Live dashboard — HTML + Chart.js
└── README.md
```

---

## Part of a Larger Pipeline

This project is **Part 1 of 3** in a connected **SA-CDT research pipeline**.

| Stage | Project | Role |
|---------|---------|------|
| 1 — Edge Detection | Decentralised Anomaly Detection in Heterogeneous Agri IoT Networks Using Edge Computing | Real-time IoT ingestion and rule-based anomaly detection |
| 2 — Threat Classification | Supply Chain Threat Classifier | ML-based multi-class cyber threat detection |
| 3 — Digital Twin Layer | Agri-Food Digital Twin Dashboard | Real-time CDT state mirroring and visualisation |

---

## Future Extensions

- Replace rule-based detection with machine learning models (Isolation Forest, LSTM)
- Add OWL ontology layer for semantic reasoning over anomaly events
- Integrate real IoT hardware (Raspberry Pi + DHT22 sensors)
- Add MQTT protocol for real-time IoT data ingestion
- Build a knowledge graph layer toward a full Semantic-Aware Cyber Digital Twin

---

## Related Publication

**Real-Time Cyber-Physical Intrusion Detection at the Industrial IoT Edge: A Lightweight Temporal Causal Explainable AI (XAI) Framework**

Raza, A. (2026). Zenodo Preprint.

DOI: 10.5281/zenodo.20539991

---

## Author

**Asad Raza**

BSc Computer Science — BIIT, PMAS Arid Agriculture University, Rawalpindi

📧 asadraza0667@gmail.com

🔗 LinkedIn

🔗 GitHub
