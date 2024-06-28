import streamlit as st

def form1():
    with st.form("Form 1"):
        var = "*"
        first_name = st.text_input(f"**First name**{var}") # Limit to 20 char
        last_name = st.text_input(f"**Last name**{var}") # Limit to 20 char
        phone_number = st.text_input(f"**Phone number**{var}") # Check that number is 10 digits
        email = st.text_input(f"**Email**{var}") # Check that the email is valid
        company = st.text_input(f"**Company**{var}") # 20 char
        form1_submit = st.form_submit_button("Next")

    if form1_submit:
        if not first_name or not last_name or not phone_number or not email or not company:
            st.warning("Please fill out all required fields.")
        else:
            st.session_state.first_name = first_name
            st.session_state.last_name = last_name
            st.session_state.phone_number = phone_number
            st.session_state.email = email
            st.session_state.company = company

def form2():
    if "first_name" in st.session_state:
        with st.form("Form 2"):
            experience_level = st.selectbox("**Experience Level**", ["Beginner (< 1 year experience)", "Junior (1 - 2 years experience)", "Intermediate (2 - 3 years experience)", "Advanced (>4 years experience)"])
            form2_submit = st.form_submit_button("Next")

        if form2_submit:
            st.session_state.experience_level = experience_level

def form3():
    if "experience_level" in st.session_state:
        with st.form("Form 3"):
            track = st.selectbox("**Which track will you be hacking on**", ["AI for video analysis in farming", "AI for Business", "AI for loss prevention"])
            form3_submit = st.form_submit_button("Next")

        if form3_submit:
            st.session_state.track = track

def form4():
    if "track" in st.session_state:
        with st.form("Form 4"):
            team = st.selectbox("**Team** | Tell us whether or not you have a team or are looking to join a team.", ["Solo hacker, I don’t need a team", "Solo hacker looking to join a team", "I already have a team"])
            form4_submit = st.form_submit_button("Next")

        if form4_submit:
            st.session_state.team = team

def form5():
    if "team" in st.session_state:
        with st.form("Form 5"):
            participation_mode = st.selectbox("**Will you be able to attend the opening and closing in-person?**", ["On-site", "Online"])
            agree = st.checkbox("By submitting this form you are agreeing to the Nerdma Hack-AI-thon T&C's")
            form5_submit = st.form_submit_button("Submit")

        if form5_submit and agree:
            st.session_state.participation_mode = participation_mode
            return True
    return False
