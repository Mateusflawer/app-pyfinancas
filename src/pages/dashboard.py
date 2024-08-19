from templates import sidebar, dashboard
from data import loader, controller
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def main():
    # Menu de navegação
    sidebar.menu()

    st.header("Bem vindo aos Gráficos!")

    df = loader.example_transactions()

    if controller.check_empty_df(df):
        st.toast("Sem dados para analisar", icon="🚨")
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

        # with st.container(border=True):
        #     # Tabela de dados
        #     st.title("Sem ideias")

if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Gráficos", "📊", "wide")
    main()