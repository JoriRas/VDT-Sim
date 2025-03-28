# VDT.py
import streamlit as st
import pandas as pd
import random

# load dataset
@st.cache_data
def load_data():
    return pd.read_csv('data/19drivers.csv')

data = load_data

#----Sidebar---
st.sidebar.title("Diagnostic Tool Controls")
show_error = st.sidebar.checkbox("Simulate Error Code", value=False)
selected_code =None
if show_error:
    selected_code = st.sidebar.selectbox("Choose Errror Code", data["DTC"].unique())

#---Main Panel---
st.title("Vehicle Diagnostic Tool Simulator")

# Simulated live data
rpm = random.randint(700, 3000)
speed = random.randint(0, 120)
engine_load = random.randint(0, 100)

st.subheader("Live Vehicle Data (Simulated)")
st.metric("RPM", f"{rpm} RPM")
st.metric("Speed", f"{speed} km/h")
st.metric("Engine Load", f"{engine_load} %")

if show_error and selected_code:
    error_info = data[data['DTC'] == selected_code]
    st.subheader("Active DTC (Diacnostiuc Trouble Code)")
    st.write(f"**Code** {selected_code}")
    st.write(f"**Description:** {error_info['Description'].values[0]}")

#Footer
st.write("----")
st.caption("Simple diagnostic Tool Simulation • Streamlit + Python")