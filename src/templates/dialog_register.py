import streamlit as st
from database import controller
from handlers import processing

tipos = controller.TIPOS

@st.dialog("Registrar Transação")
def transaction_line():
    with st.container(height=400):
        transaction = processing.Transaction()
        transaction.descricao = st.text_area("Descrição")
        transaction.efetivada = st.toggle("Efetivada", value=True)
        transaction.tipo = st.selectbox("Tipo", tipos)
        categories = controller.load_nome_categories_by_tipo(transaction.tipo)
        transaction.categoria = st.selectbox("Categoria", categories)
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
    categorie = processing.Categorie()
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
    account = processing.Account()
    account.nome = st.text_input("Nome")
    account.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        controller.insert_accounts_rows(account.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
