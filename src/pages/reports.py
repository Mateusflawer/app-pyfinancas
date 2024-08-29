from templates import reports_tables, sidebar
from utils import autenticated_helpers
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "")

TRANSACTION = "TRANSAÇÕES"
ACCOUNT = "CONTAS"
CATEGORIE = "CATEGORIAS"
CREDIT_CARD = "CARTÕES"

TABS = (TRANSACTION, CATEGORIE, ACCOUNT, CREDIT_CARD)

def main():

    sidebar.menu()

    # Carregando dados após checar que existem os arquivos

    t_transaction, t_categorie, t_account, t_credit_card = st.tabs(TABS)

    with t_transaction:
        with st.container(border=True):
            reports_tables.transactions_screen()

    with t_categorie:
        with st.container(border=True): 
            reports_tables.categories_screen()

    with t_account:
        with st.container(border=True): 
            reports_tables.accounts_screen()

    with t_credit_card:
        with st.container(border=True): 
            reports_tables.credit_card_screen()

if __name__ == "__main__":
    if autenticated_helpers.autenticated():
        # Configurações da página
        st.set_page_config("Relatórios", "📄", "wide")
        main()
    else:
        st.switch_page("pages/login.py")