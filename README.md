# 🌾 Agri-food IoT Anomaly Monitor

A real-time IoT sensor monitoring and anomaly detection dashboard for agri-food supply chains — built as a foundational prototype exploring core concepts of **Cyber Digital Twin (CDT)** architectures.

## 📌 Project Overview

This project simulates an IoT-enabled supply chain monitoring system that:
- Ingests real-time sensor data from multiple supply chain nodes (warehouses, cold storage, transport units, processing zones)
- Detects anomalies using rule-based threshold logic — temperature breaches, humidity violations, CO₂ level anomalies
- Displays a live dashboard with alert logging, historical charts, and anomaly statistics
- Demonstrates the data ingestion and anomaly detection layers central to Semantic-Aware Cyber Digital Twin frameworks

## 🔬 Research Motivation

This prototype was developed in preparation for doctoral research on **Semantic-Aware Cyber Digital Twins for Agri-food Supply Chains** — the PhD scholarship project at Maynooth University's Department of Computer Science (supervised by Dr. Mansoor Ahmed, ADAPT Centre).

The core challenge in agri-food CDT research is building systems that can:
1. Ingest heterogeneous IoT sensor streams in real-time
2. Detect anomalies that indicate cyber threats or operational failures
3. Reason semantically about the meaning of those anomalies in context

This project addresses challenge (1) and (2), providing a working prototype of the data and detection layers.

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Anomaly Detection | Rule-based threshold logic (extensible to ML) |
| Frontend Dashboard | HTML, CSS, JavaScript, Chart.js |
| Data Simulation | Python random + sensor models |

## 📊 Features

- **Live sensor readings** — temperature, humidity, CO₂ from simulated supply chain nodes
- **Real-time anomaly detection** — CRITICAL / WARNING alerts with breach details
- **Historical chart** — temperature trend over last 20 readings
- **Alert log** — timestamped anomaly log with location and breach values
- **Statistics panel** — total readings, anomaly count, anomaly rate
- **Auto-refresh** — new reading every 5 seconds

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/AsadRaza067/agri-iot-anomaly-monitor.git
cd agri-iot-anomaly-monitor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open browser
# Go to: http://localhost:5000
```

## 📁 Project Structure

```
agri-iot-anomaly-monitor/
│
├── app.py                  # Flask backend + sensor simulation + anomaly detection
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Live dashboard (HTML + Chart.js)
└── README.md
```

## 🔮 Future Extensions

- Replace rule-based detection with ML models (Isolation Forest, LSTM)
- Add OWL ontology layer for semantic reasoning over sensor data
- Integrate real IoT hardware (Raspberry Pi + DHT22 sensors)
- Add MQTT protocol for real IoT data ingestion
- Build a knowledge graph layer — moving toward full Semantic-Aware CDT

## 👤 Author

**Asad Raza**
BSc Computer Science — BIIT, PMAS Arid Agriculture University Rawalpindi
📧 asadraza0667@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/asad-raza-a007r)
