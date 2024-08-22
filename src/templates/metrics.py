import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from handlers import calculations_metrics


def dashboard_metric(df):
    """Metricas"""
    saldo, entradas, despesas = calculations_metrics.dashboard_metrics(df)

    # Metricas
    col_saldo, col_entradas, col_despesas = st.columns(3)

    with col_saldo:
        st.metric("Saldo", saldo)

    with col_entradas:
        st.metric("Entradas", entradas)

    with col_despesas:
        st.metric("Despesas", despesas)

    style_metric_cards(background_color='auto')