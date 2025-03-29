# VDT.py
import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="VDT-Sim | Vehicle Diagnostic Tool",
    page_icon="🚗",
    layout="wide"
)
st.sidebar.title("🚗 VDT-Sim")
st.sidebar.info("Developed by Jori Ras | For portfolio use")

# load dataset
@st.cache_data
def load_data():
    return pd.read_csv('data/19drivers.csv')

data = load_data

# ---Session State for Live Data History---
if "rpm_history" not in st.session_state:
    st.session_state.rpm_history = []
if "speed_history" not in st.session_state:
    st.session_state.speed_history = []
if "engine_history" not in st.session_state:
    st.session_state.engine_history = []

# --- Sample error codes ---
sample_error_codes = [
    ("P0300", "Random/Multiple Cylinder Misfire Detected"),
    ("P0420", "Catalys System Efficiency Below Threshold"),
    ("P0171", "System Too Lean (Bank 1)")
]

#----Sidebar---
st.sidebar.title("Diagnostic Tool Controls")

if st.sidebar.button("🗑️ Clear Data"):
    st.session_state.rpm_history = []
    st.session_state.speed_history = []
    st.session_state.engine_history = []
    st.success("Data history cleared!")


# --- Random Error Injection ---
if st.sidebar.button("💥 Inject Random Error"):
    random_code, description = random.choice(sample_error_codes)
    st.session_state.random_error = (random_code, description)


# --- Show Injected Error ---
if "random_error" in st.session_state:
    code, desc = st.session_state.random_error
    st.subheader("Random Injected Error Code")
    st.write(f"**Code:** {code}")
    st.write(f"**Description:** {desc}")
    if st.button("Clear Injected Error"):
        del st.session_state.random_error

#---Main Panel---
st.title("🚗 Vehicle Diagnostic Tool Simulator")

# Scan Button Animation
if st.button ("🔍 Scan Vehicle"):
    with st.spinner("Scanning Vehicle..."):
        time.sleep(2)
    st.success("Scan Complete! No immediate issues found.")

# Simulated live data
if st.button("▶️ Simulate Vehicle Data"):
    rpm = random.randint(700, 3000)
    speed = random.randint(0, 120)
    engine_load = random.randint(0, 100)

    st.session_state.rpm_history.append(rpm)
    st.session_state.speed_history.append(speed)
    st.session_state.engine_history.append(engine_load)

    st.subheader("📊 Live Vehicle Data (Simulated)")
    col1, col2, col3 = st.columns(3)
    col1.metric("RPM", f"{rpm} RPM")
    col2.metric("Speed", f"{speed} km/h")
    col3.metric("Engine Load", f"{engine_load} %")

    # ---Graphs---
    st.subheader("📈 Vehicle Data History")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("### RPM")
    rpm_df = pd.DataFrame({"RPM": st.session_state.rpm_history})
    st.line_chart(rpm_df)

with col2:
    st.write("### Speed")
    speed_df = pd.DataFrame({"Speed": st.session_state.speed_history})
    st.line_chart(speed_df)

with col3:
    st.write("### Engine Load")
    engine_df = pd.DataFrame({"Engine Load": st.session_state.engine_history})
    st.line_chart(engine_df)


#Footer
st.markdown("---")
st.markdown("© 2025 Jori Ras — Built with [Streamlit](https://streamlit.io)")
