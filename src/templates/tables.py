import streamlit as st
from database import controller
from templates import dialogs
from utils import datetime_helpers
from templates import dialogs


def transactions_screen():
    st.subheader("Transações")
    controller.create_transactions_table()
    df_transactions = controller.load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )
    st.dataframe(df_transactions, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_transaction"):
        dialogs.register_transaction()

    if col_deletar.button("❌ Deletar", key="delete_transaction"):
        dialogs.delete_transaction()

    
def categories_screen():
    st.subheader("Categorias")
    controller.create_categories_table()
    df_categories = controller.load_categories()
    st.dataframe(df_categories, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_categorie"):
        dialogs.register_categorie()

    if col_deletar.button("❌ Deletar", key="delete_categorie"):
        dialogs.delete_categorie()


def accounts_screen():
    st.subheader("Contas")
    controller.create_accounts_table()
    df_accounts = controller.load_accounts()
    st.dataframe(df_accounts, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)

    if col_registrar.button("➕ Registrar", key="register_account"):
        dialogs.register_account()

    if col_deletar.button("❌ Deletar", key="delete_account"):
        dialogs.delete_account()

        