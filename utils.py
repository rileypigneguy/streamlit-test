import streamlit as st


def menu():
    st.sidebar.page_link("main.py", label="Home", icon=":material/login:")
    st.sidebar.page_link("pages/bio.py", label="Bio", icon=":material/radio:")
