import streamlit as st
import requests

st.title("Nerdma Hack-AI-thon Applications")

# Fetch data from the Flask backend
response = requests.get('http://127.0.0.1:5000/applications')

if response.status_code == 200:
    applications = response.json()
    for app in applications:
        with st.expander(f"Applicant: {app['first_name']} {app['last_name']}"):
            st.write("First Name:", app['first_name'])
            st.write("Last Name:", app['last_name'])
            st.write("Phone Number:", app['phone_number'])
            st.write("Email:", app['email'])
            st.write("Company:", app['company'])
            st.write("Experience Level:", app['experience_level'])
            st.write("Track:", app['track'])
            st.write("Team:", app['team'])
else:
    st.error("Failed to fetch applications.")
