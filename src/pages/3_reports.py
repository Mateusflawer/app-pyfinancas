from templates import reports_tables, sidebar
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "")

TRANSACTION = "TRANSAÇÕES"
ACCOUNT = "CONTAS"
CATEGORIE = "CATEGORIAS"

TABS = (TRANSACTION, CATEGORIE, ACCOUNT)

def main():
    # Carregando dados após checar que existem os arquivos
    t_transaction, t_categorie, t_account = st.tabs(TABS)

    with t_transaction:
        with st.container(border=True):
            reports_tables.transactions_screen()

    with t_categorie:
        with st.container(border=True): 
            reports_tables.categories_screen()

    with t_account:
        with st.container(border=True): 
            reports_tables.accounts_screen()


if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Relatórios", "📄", "wide")
    sidebar.menu()
    main()