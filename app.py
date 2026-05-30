from flask import Flask, render_template, jsonify
import random
import time
from datetime import datetime, timedelta
from collections import deque

app = Flask(__name__)

# ── Simulated Sensor History ──────────────────────────────────────────────────
sensor_history = deque(maxlen=50)  # Keep last 50 readings

# Thresholds for agri-food cold chain
THRESHOLDS = {
    "temperature": {"min": 2.0, "max": 8.0},   # Celsius (cold chain)
    "humidity":    {"min": 60.0, "max": 85.0},  # Percent
    "co2_ppm":     {"min": 300,  "max": 1000},  # CO2 parts per million
}

LOCATIONS = ["Warehouse A", "Cold Storage B", "Transport Unit C", "Processing Zone D"]

def generate_sensor_reading(anomaly=False):
    """Simulate an IoT sensor reading from an agri-food supply chain node."""
    if anomaly:
        # Anomalous reading — outside safe range
        temp     = round(random.uniform(10.0, 18.0), 2)   # Too warm!
        humidity = round(random.uniform(30.0, 50.0), 2)   # Too dry!
        co2      = round(random.uniform(1200, 1800), 1)   # Too high!
    else:
        # Normal reading — within safe range
        temp     = round(random.uniform(2.5, 7.5), 2)
        humidity = round(random.uniform(62.0, 83.0), 2)
        co2      = round(random.uniform(350, 950), 1)

    return {
        "timestamp":   datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "location":    random.choice(LOCATIONS),
        "temperature": temp,
        "humidity":    humidity,
        "co2_ppm":     co2,
    }

def detect_anomalies(reading):
    """Rule-based anomaly detection for supply chain sensor data."""
    alerts = []

    if not (THRESHOLDS["temperature"]["min"] <= reading["temperature"] <= THRESHOLDS["temperature"]["max"]):
        alerts.append({
            "type":    "TEMPERATURE BREACH",
            "value":   f"{reading['temperature']}°C",
            "safe":    f"{THRESHOLDS['temperature']['min']}–{THRESHOLDS['temperature']['max']}°C",
            "level":   "CRITICAL",
        })

    if not (THRESHOLDS["humidity"]["min"] <= reading["humidity"] <= THRESHOLDS["humidity"]["max"]):
        alerts.append({
            "type":    "HUMIDITY BREACH",
            "value":   f"{reading['humidity']}%",
            "safe":    f"{THRESHOLDS['humidity']['min']}–{THRESHOLDS['humidity']['max']}%",
            "level":   "WARNING",
        })

    if not (THRESHOLDS["co2_ppm"]["min"] <= reading["co2_ppm"] <= THRESHOLDS["co2_ppm"]["max"]):
        alerts.append({
            "type":    "CO2 LEVEL BREACH",
            "value":   f"{reading['co2_ppm']} ppm",
            "safe":    f"{THRESHOLDS['co2_ppm']['min']}–{THRESHOLDS['co2_ppm']['max']} ppm",
            "level":   "WARNING",
        })

    reading["alerts"] = alerts
    reading["status"] = "ANOMALY" if alerts else "NORMAL"
    return reading

# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/reading")
def get_reading():
    """Generate a new sensor reading (10% chance of anomaly)."""
    is_anomaly = random.random() < 0.10
    raw        = generate_sensor_reading(anomaly=is_anomaly)
    reading    = detect_anomalies(raw)
    sensor_history.append(reading)
    return jsonify(reading)

@app.route("/api/history")
def get_history():
    """Return last 50 sensor readings."""
    return jsonify(list(sensor_history))

@app.route("/api/stats")
def get_stats():
    """Return summary statistics."""
    if not sensor_history:
        return jsonify({"total": 0, "anomalies": 0, "normal": 0, "anomaly_rate": 0})
    total    = len(sensor_history)
    anomalies = sum(1 for r in sensor_history if r["status"] == "ANOMALY")
    return jsonify({
        "total":        total,
        "anomalies":    anomalies,
        "normal":       total - anomalies,
        "anomaly_rate": round((anomalies / total) * 100, 1),
    })

if __name__ == "__main__":
    # Pre-populate with 20 readings
    for _ in range(20):
        raw     = generate_sensor_reading(anomaly=(random.random() < 0.10))
        reading = detect_anomalies(raw)
        sensor_history.append(reading)
    app.run(debug=True, port=5000)
