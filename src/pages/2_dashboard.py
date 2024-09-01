from templates import sidebar, metrics, graphcs
from database import controller
from utils import dataframe_helpers
import streamlit as st
import locale


locale.setlocale(locale.LC_ALL, "")

def main():
    df = controller.load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )

    # Sem dados para gerar gráficos
    if dataframe_helpers.check_empty_df(df):
        st.toast("Sem dados para gerar os gráficos", icon="🚨")
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
    sidebar.menu()
    main()