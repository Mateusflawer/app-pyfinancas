from templates import transaction, account, categorie, credit_card, sidebar
from data import controller
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

st.set_page_config("Relatórios", "📄", "wide",)

TRANSACTIONS = "TRANSAÇÕES"
ACCOUNT = "CONTAS"
CATEGORIE = "CATEGORIAS"
CREDIT_CARD = "CARTÕES DE CRÉDITO"

TABS = (TRANSACTIONS, CATEGORIE, ACCOUNT, CREDIT_CARD)

def main():
    sidebar.menu()

    st.header("Bem vindo aos Relatórios!")

    # Sempre checar se os arquvos dos dados existem antes de carrega-los
    controller.check_data_all()

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
    main()