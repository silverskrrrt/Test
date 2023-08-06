# ehsq_dashboard.py
import streamlit as st
import pandas as pd
import numpy as np

# Mock data generation
def generate_mock_data():
    return {
        "Carbon Emissions (tons)": np.random.randint(1000, 5000),
        "Water Usage (kL)": np.random.randint(500, 2000),
        "Waste Recycled (%)": np.random.randint(50, 99),
        "Energy Consumption (MWh)": np.random.randint(100, 500),
        "Safety Incidents": np.random.randint(0, 10),
        "Employee Training Hours": np.random.randint(100, 400),
        "Product Quality Issues": np.random.randint(0, 10),
        "Stakeholder Engagements": np.random.randint(1, 20)
    }

# App title and description
st.title("EHSQ KPI Dashboard for ESG Improvement")
st.write("""
This dashboard showcases key performance indicators (KPIs) that are relevant for enhancing a company's Environmental, Social, and Governance (ESG) ratings.
""")

# Generate and display KPIs
data = generate_mock_data()

for kpi, value in data.items():
    st.metric(label=kpi, value=value)

st.write("""
Note: This dashboard uses mock data. To make it functional for your organization, integrate it with your data sources and customize the KPIs accordingly.
""")

# Run the app: `streamlit run ehsq_dashboard.py`
