import streamlit as st
import numpy as np

st.title("OMEGA-X Signal Predictor")

# INPUTS
rssi = st.slider("RSSI", -120, -40, -80)
sinr = st.slider("SINR", 0, 40, 15)
traffic = st.slider("Traffic Load", 0, 100, 50)
retry = st.slider("Packet Retry", 0, 20, 5)
latency = st.slider("Latency", 0, 250, 100)

# SIMPLE AI LOGIC
score = (
    (rssi + 120) * 0.3 +
    sinr * 1.5 -
    traffic * 0.2 -
    latency * 0.1 -
    retry * 2
)

# CLASSIFICATION
if score > 45:
    signal = "Excellent"

elif score > 30:
    signal = "Good"

elif score > 15:
    signal = "Moderate"

else:
    signal = "Critical"

# CONGESTION
congestion = min(
    traffic * 0.6 +
    retry * 2 +
    latency * 0.1,
    100
)

# OUTPUT
st.subheader("Prediction Results")

st.write(f"Signal Quality: {signal}")
st.write(f"Congestion Probability: {congestion:.2f}%")
