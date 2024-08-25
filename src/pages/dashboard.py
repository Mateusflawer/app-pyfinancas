from templates import sidebar, metrics, dashboard
from utils import datetime_helpers
from database import controller
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "")

def main():
    # Menu de navegação
    sidebar.menu()

    # df = loader.example_transactions()
    controller.create_transactions_table()
    df = controller.load_transactions_per_period(*datetime_helpers.create_period(1))

    # Sem dados para gerar gráficos
    if controller.check_empty_df(df):
        st.toast("Sem dados para gerar gráficos", icon="🚨")
        st.stop()

    # Mostrando gráficos e metricas
    metrics.dashboard_metric(df)

    # Graficos categoria
    coluna_1, coluna_2 = st.columns(2)

    with coluna_1:
        # Entrada por categoria
        dashboard.entries_by_categories(df)

        # Evolução mensal
        dashboard.monthly_evolution(df)

    with coluna_2:
        # Despesas por categoria
        dashboard.expenses_by_categories(df)

        # Tabela de dados
        with st.container(border=True):
            st.dataframe()

if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Gráficos", "📊", "wide")
    main()