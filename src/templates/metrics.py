import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from handlers import calculations


def dashboard_metric(df):
    """Metricas"""
    entradas, saidas, saldo = calculations.dashboard_metrics(df)

    # Metricas
    col_entradas, col_despesas, col_saldo = st.columns(3)

    with col_entradas:
        st.metric("Entradas", entradas)

    with col_despesas:
        st.metric("Saidas", saidas)
        
    with col_saldo:
        st.metric("Saldo", saldo)

    style_metric_cards(background_color='auto')