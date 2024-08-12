import streamlit as st
from SendEmail import Emailer

st.header("Contact Me")
with st.form("E-mail Submission Forum"):
    e_mail = st.text_input("Your e-mail address: ")
    raw_message = st.text_area("Enter your message here: ", max_chars=250, height=300)
    message = f"""\
Subject: New e-mail from {e_mail}

From: {e_mail}
{raw_message}"""
    button = st.form_submit_button("Submit")
    if button:
        Emailer(message)
        st.info("Your e-mail was sent successfully!")
