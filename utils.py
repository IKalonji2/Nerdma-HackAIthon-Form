import requests
import streamlit as st

def submit_application():
    applicant_data = {
        "first_name": st.session_state.first_name,
        "last_name": st.session_state.last_name,
        "phone_number": st.session_state.phone_number,
        "email": st.session_state.email,
        "company": st.session_state.company,
        "experience_level": st.session_state.experience_level,
        "track": st.session_state.track,
        "team": st.session_state.team,
        "participation_mode": st.session_state.participation_mode  # Add participation_mode
    }
    response = requests.post('https://squid-app-mdj7h.ondigitalocean.app/submit', json=applicant_data)
    return response.status_code
