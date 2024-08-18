import streamlit as st
from data import controller, loader
from templates import sidebar, dashboard

import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

# Configurações da página
st.set_page_config("Dashboard", "📊", "wide",)

# Menu de navegação
sidebar.menu()

# Estilo da páginas
css = loader.local_css()
st.markdown(css, unsafe_allow_html=True)

controller.check_data_all()

df = loader.local_transactions()
# df = loader.example_transactions()

# Verificar se existe transações
if controller.check_empty_df(df):
    st.info("Sem transações para mostrar os gráficos", icon="❗")
    st.stop()

# Mostrando gráficos e metricas
dashboard.metrics(df)

# Graficos categoria
coluna_1, coluna_2 = st.columns(2)

with coluna_1:
    dashboard.entries_by_categories(df)

    dashboard.monthly_evolution(df)

with coluna_2:
    dashboard.expenses_by_categories(df)

    with st.container(border=True):
        # Tabela de dados
        st.title("Sem ideias")



