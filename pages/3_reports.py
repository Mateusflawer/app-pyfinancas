from templates import sidebar, tables
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
            tables.transactions()

    with t_categorie:
        with st.container(border=True): 
            tables.categories()

    with t_account:
        with st.container(border=True): 
            tables.accounts()


if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Relatórios", "📄", "wide")
    sidebar.menu()
    main()