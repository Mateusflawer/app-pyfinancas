from templates import sidebar, metrics, graphcs
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
    df = controller.load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )

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
        graphcs.entries_by_categories_dashboard(df)

        # Evolução mensal
        graphcs.monthly_evolution_dashboard(df)

    with coluna_2:
        # Despesas por categoria
        graphcs.expenses_by_categories_dashboard(df)

        # Tabela de dados
        with st.container(border=True):
            st.dataframe()

if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Gráficos", "📊", "wide")
    main()