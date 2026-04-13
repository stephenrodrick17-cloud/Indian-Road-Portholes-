import streamlit as st
import pandas as pd
import numpy as np
import requests
import cv2
from PIL import Image
import os
import time
import folium
from streamlit_folium import folium_static
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="RoadGuard AI | Command Center",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styling ---
st.markdown("""
<style>
    .main {
        background-color: #020617;
        color: #f8fafc;
    }
    .stApp {
        background: radial-gradient(circle at top right, #0f172a, #020617);
    }
    .stSidebar {
        background-color: #0f172a !important;
        border-right: 1px solid #1e293b;
    }
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 900 !important;
        letter-spacing: -0.05em !important;
    }
    .stButton>button {
        background-color: #f97316;
        color: white;
        border-radius: 12px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        border: none;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #ea580c;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(249, 115, 22, 0.4);
    }
</style>
""", unsafe_allow_name=True)

# --- App State / Navigation ---
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/5903/5903561.png", width=80)
    st.title("RoadGuard AI")
    st.caption("ULTRA-PRECISION MONITORING")
    st.divider()
    
    st.session_state.page = st.radio(
        "Navigation",
        ["Dashboard", "AI Detection", "Road SOS", "Incident Map"],
        index=0
    )
    
    st.divider()
    st.info("System Status: **NOMINAL**\n\nSatellite Link: **CONNECTED**")

# --- Content Sections ---

if st.session_state.page == "Dashboard":
    st.title("COMMAND CENTER 📡")
    st.subheader("Global Infrastructure Intelligence")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Anomalies", "1,284", "+12.5%")
    with col2:
        st.metric("Critical Defects", "42", "-2")
    with col3:
        st.metric("Units En-Route", "12", "+3")
    with col4:
        st.metric("Avg Response Time", "14 min", "-2m")

    st.divider()
    
    st.markdown("### 📈 Tactical Activity")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3) * [10, 5, 2] + [50, 20, 5],
        columns=["Detections", "Repairs", "Severe Errors"]
    )
    st.area_chart(chart_data)

elif st.session_state.page == "AI Detection":
    st.title("AI PRECISION DETECTION 📸")
    st.write("Upload infrastructure footage for automated damage analysis.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Source Feed", use_column_width=True)
        
        with col2:
            st.markdown("### Scanning for Anomalies...")
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
            
            # Simulated Detection Logic
            st.success("✅ Analysis Complete")
            st.write("**Detected Anomalies:**")
            st.write("- 🕳️ **Pothole (Severe)**: Conf. 94.2%")
            st.write("- 🏗️ **Faded Markings**: Conf. 88.1%")
            
            st.info("Recommendation: Dispatch Maintenance Unit (Alpha-6)")

elif st.session_state.page == "Road SOS":
    st.title("EMERGENCY PROTOCOL (SOS) 🚨")
    
    st.error("❗ ONE-TAP EMERGENCY BROADCAST")
    if st.button("TRIGGER SOS ALERT"):
        st.warning("🚨 EMERGENCY SIGNAL TRANSMITTED TO REGIONAL HUB")
        st.balloons()
    
    st.divider()
    
    st.markdown("### 🚁 Live Response Units")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Unit ID: PATROL-704**")
        st.progress(65)
        st.caption("Distance: 2.1km | Status: EXECUTING INTERCEPTION")
    with col2:
        st.write("**Unit ID: MED-12**")
        st.progress(40)
        st.caption("Distance: 4.5km | Status: RESPONDING")

elif st.session_state.page == "Incident Map":
    st.title("TACTICAL OVERLAY 🌍")
    
    # Location data
    m = folium.Map(location=[19.0760, 72.8777], zoom_start=12, tiles='CartoDB dark_matter')
    
    # Add some markers
    incidents = [
        {"name": "Pothole Cluster", "loc": [19.08, 72.88], "color": "red"},
        {"name": "Structural Issue", "loc": [19.09, 72.86], "color": "orange"},
        {"name": "Road Work", "loc": [19.07, 72.89], "color": "blue"},
    ]
    
    for inc in incidents:
        folium.Marker(
            inc["loc"], 
            popup=inc["name"],
            icon=folium.Icon(color=inc["color"], icon='info-sign')
        ).add_to(m)
        
    folium_static(m, width=1200)

# --- Footer ---
st.divider()
st.caption("© 2024 RoadGuard AI Systems. Secure Satellite Link v1.2.0")
