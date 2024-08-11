import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd

col1, col2 = st.columns(2)
with col1:
    st.image(r"C:\Users\LENOVO\Documents\Python\Projects\Portfolio-Project\Self.png")
with col2:
    st.title("My Info")
    content = """
    Hi! My name is Naman Sharma and I am a college student studying at Amity University,Noida in India.
    """
    st.info(content)

content2 = """
Below you can find some Python Projects built by me.
"""
st.info(content2)

df = pd.read_csv(r"C:\Users\LENOVO\Documents\Python\Projects\Portfolio-Project\data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(r"C:\Users\LENOVO\Documents\Python\Projects\Portfolio-Project\images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(r"C:\Users\LENOVO\Documents\Python\Projects\Portfolio-Project\images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")
