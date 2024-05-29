import streamlit as st

def menu():
    st.sidebar.page_link("pages/dashboard.py")
    st.sidebar.page_link("pages/reports.py")
    st.sidebar.page_link("pages/settings.py")

