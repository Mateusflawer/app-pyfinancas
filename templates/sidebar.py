import streamlit as st

def menu():
    st.sidebar.page_link("pages/dashboard.py", label="Gráficos", icon="📊")
    st.sidebar.page_link("pages/reports.py", label="Relatórios", icon="📄")
    st.sidebar.page_link("pages/settings.py", label="Configurações", icon="⚙️")