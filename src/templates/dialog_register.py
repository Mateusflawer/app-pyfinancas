import streamlit as st
from database import controller
from handlers import class_processing

tipos = (controller.ENTRADA, controller.DESPESA)

@st.dialog("Registrar Transação")
def transaction_line():
    with st.container(height=400):
        transaction = class_processing.Transaction()

        transaction.descricao = st.text_area("Descrição")

        col_credit, col_efetivada = st.columns(2)
        credit = col_credit.toggle("Crédito")
        transaction.efetivada = col_efetivada.toggle("Efetivada", value=True)
        
        if credit:
            transaction.tipo = st.selectbox("Tipo", [controller.DESPESA], disabled=credit)
        else:
            transaction.tipo = st.selectbox("Tipo", tipos, disabled=credit)

        categories = controller.load_nome_categories_by_tipo(transaction.tipo)
        transaction.categoria = st.selectbox("Categoria", categories)
    
        if credit:
            cards = controller.load_nome_credit_cards()
            transaction.credit_card = st.selectbox("Cartão de crédito", cards)
        else:
            accounts = controller.load_nome_accounts()
            transaction.conta = st.selectbox("Conta", accounts)

        transaction.data = st.date_input("Data", format="DD/MM/YYYY")
        transaction.valor = st.number_input("Valor")

    col_salvar, col_cancelar = st.columns(2)

    if col_salvar.button("Salvar ✅"):
        controller.insert_transactions_rows(transaction.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
        

@st.dialog("Registrar Categoria")
def categorie_line():
    categorie = class_processing.Categorie()
    categorie.nome = st.text_input("Nome")
    categorie.tipo = st.selectbox("Tipo", controller.TIPOS)

    categorie.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    col_salvar, col_cancelar = st.columns(2)

    if col_salvar.button("Salvar ✅"):
        controller.insert_categories_rows(categorie.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.dialog("Registrar Conta")
def account_line():
    account = class_processing.Account()
    account.nome = st.text_input("Nome")

    account.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    col_salvar, col_cancelar = st.columns(2)

    if col_salvar.button("Salvar ✅"):
        controller.insert_accounts_rows(account.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.dialog("Registrar Cartão")
def credit_card_line():
    credit_card = class_processing.CreditCard()
    credit_card.nome = st.text_input("Nome")

    credit_card.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    credit_card.fechamento = st.number_input("Fechamento", step=0, min_value=1, max_value=31)
    credit_card.vencimento = st.number_input("Vencimento", step=0, min_value=1, max_value=31)
    credit_card.limite = st.number_input("Limite", step=10)

    col_salvar, col_cancelar = st.columns(2)

    if col_salvar.button("Salvar ✅"):
        controller.insert_credit_cards_rows(credit_card.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()