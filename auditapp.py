# baudokumentation_app.py
import streamlit as st
import pandas as pd
import numpy as np

# Mock data generation for IoT
def generate_iot_data():
    return {
        "Temperature (°C)": np.random.uniform(15, 30),
        "Humidity (%)": np.random.uniform(40, 70),
        "Air Quality (AQI)": np.random.randint(10, 100)
    }

# App title and description
st.title("Baudokumentation with IoT Data Display")
st.write("Enter Baudokumentation audit details and view sample IoT data below.")

# Form for Baudokumentation
with st.form(key='bauform'):
    st.subheader("Baudokumentation Audit Entry")
    project_name = st.text_input("Project Name:")
    date = st.date_input("Date")
    location = st.text_input("Location:")
    inspector_name = st.text_input("Inspector Name:")
    comments = st.text_area("Comments:")
    submit_data = st.form_submit_button("Add Entry")

# Display Baudokumentation data if submitted
if submit_data:
    st.subheader("Submitted Baudokumentation Audit Details")
    st.write("Project Name:", project_name)
    st.write("Date:", date)
    st.write("Location:", location)
    st.write("Inspector Name:", inspector_name)
    st.write("Comments:", comments)

# Display IoT data
st.subheader("Sample IoT Data")
iot_data = generate_iot_data()
for kpi, value in iot_data.items():
    st.metric(label=kpi, value=f"{value:.2f}")

# For enhanced visualization, we can create charts for IoT data:
iot_df = pd.DataFrame([iot_data])

st.bar_chart(iot_df)

# Run the app: `streamlit run baudokumentation_app.py`
