# FAST ADAPTIVE SIGNAL OUTCOME PREDICTOR
# -------------------------------------
# Install:
# pip install streamlit numpy

import streamlit as st
import numpy as np

# =====================================================
# PAGE
# =====================================================

st.set_page_config(
    page_title="Fast Adaptive Signal Predictor",
    layout="centered"
)

st.title("Fast Adaptive Signal Outcome Predictor")

st.write(
    "Adaptive AI-based wireless signal prediction system"
)

# =====================================================
# INPUTS
# =====================================================

rssi = st.slider("RSSI", -120, -40, -75)
sinr = st.slider("SINR", 0, 40, 18)
traffic = st.slider("Traffic Load", 0, 100, 55)
latency = st.slider("Latency", 0, 300, 90)
packet_loss = st.slider("Packet Loss %", 0, 100, 10)

# =====================================================
# FAST ADAPTIVE AI ENGINE
# =====================================================

signal_score = (
    (rssi + 120) * 0.35 +
    sinr * 1.8 -
    traffic * 0.25 -
    latency * 0.08 -
    packet_loss * 0.5
)

# =====================================================
# SIGNAL OUTCOME
# =====================================================

if signal_score >= 50:
    outcome = "Excellent Stable Signal"
    status = "Low Interference"

elif signal_score >= 35:
    outcome = "Good Adaptive Signal"
    status = "Minor Congestion"

elif signal_score >= 20:
    outcome = "Moderate Signal Risk"
    status = "Possible Interference"

else:
    outcome = "Critical Signal Failure"
    status = "High Congestion"

# =====================================================
# CONGESTION PROBABILITY
# =====================================================

congestion_probability = min(
    (
        traffic * 0.5 +
        latency * 0.15 +
        packet_loss * 0.8
    ),
    100
)

# =====================================================
# CHANNEL OPTIMIZATION
# =====================================================

channels = [
    "CH-1",
    "CH-6",
    "CH-11",
    "5G Sub-6",
    "5G mmWave"
]

best_channel = np.random.choice(channels)

# =====================================================
# OUTPUT
# =====================================================

st.subheader("Prediction Results")

st.success(f"Signal Outcome: {outcome}")

st.write(f"Network Status: {status}")

st.write(
    f"Congestion Probability: "
    f"{congestion_probability:.2f}%"
)

st.write(f"Recommended Channel: {best_channel}")

# =====================================================
# LIVE ADAPTIVE STATUS
# =====================================================

if congestion_probability > 80:
    st.error(
        "AI Recommendation: Immediate load balancing required"
    )

elif congestion_probability > 50:
    st.warning(
        "AI Recommendation: Adaptive optimization suggested"
    )

else:
    st.info(
        "AI Recommendation: Network operating normally"
    )

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "OMEGA-X Adaptive Wireless Intelligence"
)
