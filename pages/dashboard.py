import streamlit as st
import data
import utils
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

# Configurações da página
st.set_page_config("Dashboard", "📊", "wide",)

# Menu de navegação
utils.helpers.menu()

# Estilo da páginas
css = data.loader.local_css()
st.markdown(css, unsafe_allow_html=True)

data.controller.check_data_all()

df = data.loader.local_transactions()
# df = data.loader.example_transactions()

# Verificar se existe transações
if data.controller.check_empty_df(df):
    st.info("Sem transações para mostrar os gráficos", icon="❗")
    st.stop()

# Mostrando gráficos e metricas
utils.metrics.dashboard(df)
utils.graph.dashboard(df)
