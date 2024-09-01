import streamlit as st
from database import controller
from utils import datetime_helpers
from templates import dialog_register, dialog_delete


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
        dialog_register.transaction_line()

    if col_deletar.button("❌ Deletar", key="delete_transaction"):
        dialog_delete.transaction_line()

    
def categories_screen():
    st.subheader("Categorias")
    controller.create_categories_table()
    df_categories = controller.load_categories()
    st.dataframe(df_categories, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_categorie"):
        dialog_register.categorie_line()

    if col_deletar.button("❌ Deletar", key="delete_categorie"):
        dialog_delete.categorie_line()


def accounts_screen():
    st.subheader("Contas")
    controller.create_accounts_table()
    df_accounts = controller.load_accounts()
    st.dataframe(df_accounts, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)

    if col_registrar.button("➕ Registrar", key="register_account"):
        dialog_register.account_line()

    if col_deletar.button("❌ Deletar", key="delete_account"):
        dialog_delete.account_line()

        