# Vehicle-Diagnostic-Tool

Vehicle Diagnostic Tool Simulation

A simple, interactive Vehicle Diagnostic Tool Simulator built using Streamlit + Python.
This project simulates real-time vehicle data like RPM, Speed, and Engine Load, and allows you to simulate OBD-II error codes from a dataset.

Real-time simulation of RPM, Speed, and Engine Load data

Live updating graphs of vehicle data history

"🔍 Scan Vehicle" button with loading animation

Simulate active Diagnostic Trouble Codes (DTC)

Simple & lightweight web interface

Installation
1.Clone the repository
git clone https://github.com/JoriRas/Vehicle-Diagnostic-Tool.git
cd vehicle-diagnostic-tool

2.Install dependencies
pip install -r requirements.txt

3. Add ONB Dataset
   Place your obd_dataset.csv inside the /data folder.

Run the App
streamlit run app.py
Open your browser at http://localhost:8501

Future Improvements:

"Clear Data" button

Random error code injection option

Export diagnostic report as PDF

Mobile-friendly UI
