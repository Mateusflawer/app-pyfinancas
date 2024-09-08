import streamlit as st
from database import controller
from templates import dialogs
from utils import datetime_helpers
from templates import dialogs


@st.fragment()
def transactions():
    st.subheader("Transações")
    controller.create_transactions_table()
    df_transactions = controller.load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )
    st.dataframe(
        df_transactions.drop(columns=['id']), 
        hide_index=True, use_container_width=True
    )
    col_registrar, col_editar, col_deletar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_transaction"):
        dialogs.register_transaction()

    if col_editar.button('✏️ Editar', key='editar-transaction'):
        dialogs.edit_transaction()

    if col_deletar.button("❌ Deletar", key="delete_transaction"):
        dialogs.delete_transaction()

@st.fragment()
def categories():
    st.subheader("Categorias")
    controller.create_categories_table()
    df_categories = controller.load_categories()
    st.dataframe(
        df_categories.drop(columns=['id']), 
        hide_index=True, use_container_width=True
    )
    col_registrar, col_editar, col_deletar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_categorie"):
        dialogs.register_categorie()

    if col_editar.button('✏️ Editar', key='editar-categorie'):
        dialogs.edit_categorie()

    if col_deletar.button("❌ Deletar", key="delete_categorie"):
        dialogs.delete_categorie()

@st.fragment()
def accounts():
    st.subheader("Contas")
    controller.create_accounts_table()
    df_accounts = controller.load_accounts()
    st.dataframe(
        df_accounts.drop(columns=['id']), 
        hide_index=True, use_container_width=True
    )
    col_registrar, col_editar, col_deletar = st.columns(3)

    if col_registrar.button("➕ Registrar", key="register_account"):
        dialogs.register_account()

    if col_editar.button('✏️ Editar', key='editar-account'):
        dialogs.edit_account()
        
    if col_deletar.button("❌ Deletar", key="delete_account"):
        dialogs.delete_account()

        