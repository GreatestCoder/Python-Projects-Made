import streamlit as st
st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image(r"C:\Users\LENOVO\Documents\Python\Projects\Portfolio-Project\2.png")
with col2:
    st.title("My Info")
    content = """
    Blah Blah Blah
    """
    st.info(content)