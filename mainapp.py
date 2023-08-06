# app.py
import streamlit as st

# Title and Introduction
st.title("Baudokumentation Audit")
st.write("Enter details for the Baudokumentation audit below:")

# Form fields
with st.form(key='bauform'):
    project_name = st.text_input("Project Name:")
    date = st.date_input("Date")
    location = st.text_input("Location:")
    inspector_name = st.text_input("Inspector Name:")
    comments = st.text_area("Comments:")

    # Submit button
    submit = st.form_submit_button("Submit")

# Display the submitted information
if submit:
    st.subheader("Submitted Baudokumentation Audit Details")
    st.write("Project Name:", project_name)
    st.write("Date:", date)
    st.write("Location:", location)
    st.write("Inspector Name:", inspector_name)
    st.write("Comments:", comments)
