import os
import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# --- CONFIGURATION ---
st.set_page_config(page_title="Epilepsy Risk Dashboard", layout="centered")

# Use Pathlib for more robust cross-platform path handling
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR.parent / "models" / "model.pkl"

# --- MODEL LOADING ---
@st.cache_resource
def load_model(path):
    if not os.path.exists(path):
        st.error(f"Model file not found at: {path}. Please run your notebook to train and save the model first.")
        st.stop()
    return joblib.load(path)

model = load_model(model_path)

# --- UI ELEMENTS ---
st.title("Epilepsy Seizure Risk Dashboard")
st.markdown("Enter patient metrics below to assess the simulated risk of a seizure event.")

with st.sidebar:
    st.header("Patient Metrics")
    # Features must match the EXACT order from your X_train in the notebook
    age = st.slider("Age", 0, 100, 25)
    sleep = st.slider("Sleep Hours (Last 24h)", 0.0, 12.0, 8.0)
    stress = st.select_slider("Stress Level", options=list(range(1, 11)), value=5)
    temp = st.number_input("Body Temperature (°C)", value=37.0, step=0.1)
    missed_med = st.checkbox("Missed Medication?")
    alcohol = st.checkbox("Alcohol Intake?")
    screen_time = st.slider("Screen Time (Hours)", 0, 16, 4)
    activity = st.slider("Physical Activity (Hours/Week)", 0, 20, 5)

# --- PREDICTION LOGIC ---
# Convert booleans to 1/0 for the model
input_features = np.array([[
    age, sleep, stress, temp, 
    1 if missed_med else 0, 
    1 if alcohol else 0, 
    screen_time, activity
]])

if st.button("Analyze Risk", use_container_width=True):
    # Get probability if the model supports it, else just class
    try:
        prob = model.predict_proba(input_features)[0][1]
        risk_score = f"{prob:.1%}"
        
        if prob > 0.7:
            st.error(f"HIGH RISK: {risk_score} probability of seizure.")
        elif prob > 0.3:
            st.warning(f"MODERATE RISK: {risk_score} probability of seizure.")
        else:
            st.success(f"LOW RISK: {risk_score} probability of seizure.")
    except AttributeError:
        # Fallback if probability isn't available
        prediction = model.predict(input_features)
        if prediction[0] == 1:
            st.error("HIGH RISK: Seizure event predicted.")
        else:
            st.success("LOW RISK: No seizure event predicted.")

st.divider()
st.caption("Note: This dashboard uses simulated data and is for educational purposes only.")

