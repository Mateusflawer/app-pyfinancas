import streamlit as st
from data import controller, loader
from utils import helpers, metrics, graph
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

# Configurações da página
st.set_page_config("Dashboard", "📊", "wide",)

# Menu de navegação
helpers.menu()

# Estilo da páginas
css = loader.local_css()
st.markdown(css, unsafe_allow_html=True)

controller.check_data()

df = loader.local_transactions()
# df = loader.example_transactions()

# Verificar se existe transações
if controller.check_empty_df(df):
    st.info("Sem transações para mostrar os gráficos", icon="❗")
    st.stop()

# Mostrando gráficos e metricas
metrics.dashboard(df)
graph.dashboard(df)
