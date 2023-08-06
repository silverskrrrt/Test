# ehsq_dashboard.py
import streamlit as st
import pandas as pd
import numpy as np

# Mock data generation
def generate_mock_data(adjustment_factor):
    return {
        "Carbon Emissions (tons)": np.random.randint(1000, 5000) * adjustment_factor,
        "Water Usage (kL)": np.random.randint(500, 2000) * adjustment_factor,
        "Waste Recycled (%)": np.random.randint(50, 99),
        "Energy Consumption (MWh)": np.random.randint(100, 500) * adjustment_factor,
        "Safety Incidents": np.random.randint(0, 10),
        "Employee Training Hours": np.random.randint(100, 400) * adjustment_factor,
        "Product Quality Issues": np.random.randint(0, 10),
        "Stakeholder Engagements": np.random.randint(1, 20) * adjustment_factor
    }

# App title and description
st.title("Interactive EHSQ KPI Dashboard for ESG Improvement")
st.write("""
This dashboard showcases key performance indicators (KPIs) with interactive sliders and visualizations.
""")

# Slider for adjusting mock data
adjustment_factor = st.slider("Adjustment Factor for KPIs", 0.5, 2.0, 1.0)
data = generate_mock_data(adjustment_factor)

# Display KPIs and visualizations
for kpi, value in data.items():
    st.subheader(kpi)
    st.metric(label=kpi, value=value)
    
    if kpi in ["Carbon Emissions (tons)", "Water Usage (kL)", "Energy Consumption (MWh)", "Employee Training Hours", "Stakeholder Engagements"]:
        st.bar_chart([value, value / adjustment_factor])
    
    elif kpi == "Waste Recycled (%)":
        st.line_chart([value, value / adjustment_factor])
    
    elif kpi in ["Safety Incidents", "Product Quality Issues"]:
        st.pie_chart([value, 10 - value])

st.write("""
Note: This dashboard uses mock data for demonstration. To make it functional for your organization, integrate it with your data sources and customize the KPIs accordingly.
""")

# Run the app: `streamlit run ehsq_dashboard.py`
