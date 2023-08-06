# audit_app.py
import streamlit as st
import pandas as pd

# Create or load data
try:
    # Load previous data
    data = pd.read_csv('audit_data.csv')
except FileNotFoundError:
    # Or initialize an empty dataframe
    data = pd.DataFrame(columns=["Date", "Auditor", "Department", "Findings", "Recommendations"])

# App Title
st.title("Simple Auditing App")

# Form for new audit entry
with st.form(key='audit_form'):
    st.subheader("New Audit Entry")
    date = st.date_input("Audit Date")
    auditor = st.text_input("Auditor's Name")
    department = st.text_input("Department")
    findings = st.text_area("Findings")
    recommendations = st.text_area("Recommendations")

    submit_data = st.form_submit_button("Add Entry")

# Handle submitted data
if submit_data:
    new_data = {"Date": date, "Auditor": auditor, "Department": department, 
                "Findings": findings, "Recommendations": recommendations}
    data = data.append(new_data, ignore_index=True)
    data.to_csv('audit_data.csv', index=False)

# Display data
st.subheader("Audit Entries")
st.write(data)

