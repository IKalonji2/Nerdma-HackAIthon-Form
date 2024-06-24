import streamlit as st

st.set_page_config(layout="wide")

from forms import form1, form2, form3, form4, form5
from utils import submit_application
from header_html import header_html, centered_css

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown(header_html, unsafe_allow_html=True)
st.markdown(centered_css, unsafe_allow_html=True)
st.write('<div class="content">', unsafe_allow_html=True)

# Check if the form has been submitted
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Create three columns
col1, col2, col3 = st.columns([0.5, 2, 0.5])

with col2:
    if st.session_state.form_submitted:
        st.markdown('''
        <div class="centered-message">
            <h2>Thank you for registering, we will be in contact soon with more details on the Hack-AI-thon</h2>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.text("")
        st.text("")
        st.text("")
        st.write("**Welcome to annual Nerdma Hack-AI-Thon** We need a few details to register you as a hacker.")
        form1()
        form2()
        form3()
        form4()

        if form5():
            status_code = submit_application()
            if status_code == 201:
                st.session_state.form_submitted = True
                st.experimental_rerun()
            else:
                st.error("Failed to submit the application.")

st.write('</div>', unsafe_allow_html=True)
