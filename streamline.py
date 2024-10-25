import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Simulate data for the graph
days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
hot_flash_intensity = [2, 3, 4, 3, 2, 2, 1]

# Page 1: Home
def home_page():
    st.title("Welcome Astrid")
    st.subheader("How are you today?")
    
    st.metric(label="Daily Hot Flashes", value="5-7")
    st.metric(label="Deep Sleep", value="2 Hours")
    
    # Circular Progress Indicator Simulation
    st.write("### Progress: beginning of menopause")
    st.progress(0.75)  # 75% progress (just for demonstration)
    
    st.write("### Daily Recommendation")
    st.info("Try avoiding alcohol today")
    
    st.write("### Daily Reminder")
    st.warning("Don't forget to stay active")

# Page 2: Symptoms Tracker
def symptoms_tracker_page():
    st.title("25 October 2024")
    st.subheader("Symptoms Tracker")
    
    # Hot Flash Graph
    st.write("### Hot Flashes")
    fig, ax = plt.subplots()
    ax.bar(days, hot_flash_intensity, color='lightblue')
    ax.set_ylabel('Intensity')
    ax.set_xlabel('Days')
    st.pyplot(fig)
    
    # Other Metrics
    st.metric(label="Activity Score", value="1 workout")
    st.metric(label="Nutrition Score", value="1853 calories")
    st.metric(label="Sleep Score", value="5h slept last night")
    
    # Medication Reminder
    st.write("### Medication Reminder")
    medications = pd.DataFrame({
        'Medication': ['Klimadynon Habit', 'Calcium Habit', 'Johanneskraut Habit'],
        'Status': ['Ongoing', 'Ongoing', 'Ongoing']
    })
    st.table(medications)

# Navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Symptoms Tracker"])

if page == "Home":
    home_page()
else:
    symptoms_tracker_page()
