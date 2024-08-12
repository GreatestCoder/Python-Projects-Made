import streamlit as st

st.header("Contact Me")
with st.form("E-mail Submission Forum"):
    e_mail = st.text_input("Your e-mail address: ")
    message = st.text_area("Enter your message here: ", max_chars=250, height=300)
    button = st.form_submit_button("Submit")
