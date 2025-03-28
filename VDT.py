# VDT.py
import streamlit as st
import pandas as pd
import random
import time

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
if "engine_load_history" not in st.session_state:
    st.session_state.engine_history = []


#----Sidebar---
st.sidebar.title("Diagnostic Tool Controls")
show_error = st.sidebar.checkbox("Simulate Error Code", value=False)
selected_code =None
if show_error:
    selected_code = st.sidebar.selectbox("Choose Errror Code", data["DTC"].unique())

#---Main Panel---
st.title("Vehicle Diagnostic Tool Simulator")

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

    history_df = pd.DataFrame({
        "RPM": st.session_state.rpm_history,
        "Speed": st.session_state.speed_history,
        "Engine_Load": st.session_state.engine_history
    })

    st.line_chart(history_df)

if show_error and selected_code:
    error_info = data[data['DTC'] == selected_code]
    st.subheader("Active DTC (Diacnostiuc Trouble Code)")
    st.write(f"**Code** {selected_code}")
    st.write(f"**Description:** {error_info['Description'].values[0]}")

#Footer
st.write("----")
st.caption("Simple diagnostic Tool Simulation • Streamlit + Python")