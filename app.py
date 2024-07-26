import streamlit as st

st.set_page_config(layout="wide")

# from forms import form1, form2, form3, form4, form5
# from utils import submit_application
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

# Style for the card
card_style = """
    <style>
    .card {
        background: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin: 50px auto;
        max-width: 600px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """

st.markdown(card_style, unsafe_allow_html=True)

# Message to inform applicants that applications are closed
applications_closed_message = """
<div class="card">
    <h2>Thank You for Your Interest</h2>
    <p>We appreciate your enthusiasm and willingness to participate in our program. However, we regret to inform you that the applications are now closed.</p>
    <p>We encourage you to stay connected with us for future opportunities. Thank you once again for your interest!</p>
</div>
"""
st.markdown(applications_closed_message, unsafe_allow_html=True)
