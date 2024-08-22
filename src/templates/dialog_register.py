import streamlit as st
from database import controller
from utils import datetime_helpers

@st.dialog("Registrar Transação")
def transaction_line():
    with st.container(height=400):
        with st.spinner("Carregando dados..."):
            df_categories = controller.load_categories_per_period(*datetime_helpers.create_period(1))
            df_accounts = controller.load_accounts_per_period(*datetime_helpers.create_period(1))
            df_credit_cards = controller.load_credit_cards_per_period(*datetime_helpers.create_period(1))

        transaction = controller.Transaction()

        transaction.descricao = st.text_area("Descrição")

        credito = st.toggle("Crédito?")

        if not credito:
            transaction.tipo = st.selectbox("tipo", controller.TIPOS)
        else:
            transaction.tipo = controller.TIPOS[1] # Despesa
        
        if transaction.tipo == controller.TIPOS[0]: # Se entrada
            categorias = df_categories[df_categories["tipo"]==controller.TIPOS[0]]["nome"].unique()
        else:
            categorias = df_categories[df_categories["tipo"]==controller.TIPOS[1]]["nome"].unique()

        transaction.categoria = st.selectbox("Categoria", categorias)
    
        if credito:
            transaction.credit_card = st.selectbox("Cartão de crédito", df_credit_cards["nome"].unique())
        else:
            transaction.conta = st.selectbox("Conta", df_accounts["nome"].unique())

        transaction.data = st.date_input("Data", format="DD/MM/YYYY")
        transaction.valor = st.number_input("Valor")

    if st.button("Salvar"):
        # controller.insert_transactions_rows(transaction.dataframe)
        st.rerun()

@st.dialog("Registrar Categoria")
def categorie_line():
    categorie = controller.Categorie()
    categorie.nome = st.text_input("Nome")
    categorie.tipo = st.selectbox("Tipo", controller.TIPOS)

    categorie.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    if st.button("Salvar"):
        # controller.insert_categories_rows(categorie.dataframe)
        st.rerun()

@st.dialog("Registrar Conta")
def account_line():
    account = controller.Account()
    account.nome = st.text_input("Nome")

    account.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    if st.button("Salvar"):
        # controller.insert_accounts_rows(account.dataframe)
        st.rerun()

@st.dialog("Registrar Cartão")
def credit_card_line():
    credit_card = controller.CreditCard()
    credit_card.nome = st.text_input("Nome")

    credit_card.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    credit_card.fechamento = st.number_input("Fechamento", step=0, min_value=1, max_value=31)
    credit_card.vencimento = st.number_input("Vencimento", step=0, min_value=1, max_value=31)
    credit_card.limite = st.number_input("Limite", step=10)

    if st.button("Salvar"):
        # controller.insert_credit_cards_rows(credit_card.dataframe)
        st.rerun()
