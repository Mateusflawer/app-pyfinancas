import streamlit as st
from database import controller
from handlers import processing
from utils import dataframe_helpers

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


@st.dialog("Excluir transação", width="large")
def transaction_line():
    df = controller.load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )
    
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
    
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df = st.data_editor(df, use_container_width=True, hide_index=True)
    
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        df = df[df["Excluir"]==True]
        ids = df["id"].tolist()
        controller.delete_rows_transactions_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.dialog("Excluir categoria", width="large")
def categorie_line():
    df = controller.load_categories()
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    col_excluir, col_cancelar = st.columns(2)
    
    if col_excluir.button("Excluir ✅"):
        df_result = df_result[df_result["Excluir"]==True]
        ids = df_result["id"].tolist()
        controller.delete_rows_categories_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()

@st.dialog("Excluir conta", width="large")
def account_line():
    df = controller.load_accounts()
    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)
        
        if not dataframe_helpers.check_empty_df(df):
            df = df.copy()
            
    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        df_result = df_result[df_result["Excluir"]==True]
        ids = df_result["id"].tolist()
        controller.delete_rows_accounts_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
