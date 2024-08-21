from templates import transaction, account, categorie, credit_card, sidebar
from data import controller
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

TRANSACTIONS = "TRANSAÇÕES"
ACCOUNT = "CONTAS"
CATEGORIE = "CATEGORIAS"
CREDIT_CARD = "CARTÕES DE CRÉDITO"

TABS = (TRANSACTIONS, CATEGORIE, ACCOUNT, CREDIT_CARD)

def main():

    sidebar.menu()

    # Carregando dados após checar que existem os arquivos

    t_transaction, t_categorie, t_account, t_credit_card = st.tabs(TABS)

    with t_transaction:
        with st.container(border=True): 
            transaction.transactions_screen()

    with t_categorie:
        with st.container(border=True): 
            categorie.categories_screen()

    with t_account:
        with st.container(border=True): 
            account.accounts_screen()

    with t_credit_card:
        with st.container(border=True): 
            credit_card.credit_card_screen()

if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Relatórios", "📄", "wide")
    main()