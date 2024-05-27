import streamlit as st
from utils import calculations

def dashboard(df):
    saldo, entradas, despesas = calculations.dashboard_metrics(df)

    # Metricas
    col_saldo, col_entradas, col_despesas = st.columns(3)

    with col_saldo.container(border=True):
        st.metric("Saldo", saldo)

    with col_entradas.container(border=True):
        st.metric("Entradas", entradas)

    with col_despesas.container(border=True):
        st.metric("Despesas", despesas)