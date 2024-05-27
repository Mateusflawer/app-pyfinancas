import streamlit as st
from data import data_loader
from utils import metrics, graph

# Configurações da página
st.set_page_config("Dashboard", "📊", "wide",)

# Caminho do css da página
LOCAL_CSS = "app-pyfinancas\\assets\\styles.css"

# Estilo da página
css = data_loader.local_css(LOCAL_CSS)
st.markdown(css, unsafe_allow_html=True)

# Carregando dados para a dashboard
df = data_loader.example_transactions()

# Mostrando gráficos e metricas
metrics.dashboard(df)
graph.dashboard(df)
