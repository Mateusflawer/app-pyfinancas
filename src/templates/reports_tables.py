import streamlit as st
from database import controller
from utils import datetime_helpers
from templates import dialog_register, dialog_delete


def transactions_screen():
    st.subheader("Transações")
    controller.create_transactions_table()
    df_transactions = controller.load_transactions_per_period(*datetime_helpers.create_period(1))
    # df_transactions["Data"] = df_transactions["Data"].apply(helpers.format_data_br)
    st.dataframe(df_transactions, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_transaction"):
        dialog_register.transaction_line()

    if col_deletar.button("❌ Deletar", key="delete_transaction"):
        dialog_delete.transaction_line()


def categories_screen():
    st.subheader("Categorias")
    controller.create_categories_table()
    df_categories = controller.load_categories_per_period(*datetime_helpers.create_period(1))
    # df_categories["Data"] = df_categories["Data"].apply(helpers.format_data_br)
    st.dataframe(df_categories, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_categorie"):
        dialog_register.categorie_line()

    if col_deletar.button("❌ Deletar", key="delete_categorie"):
        dialog_delete.categorie_line()


def accounts_screen():
    st.subheader("Contas")
    controller.create_accounts_table()
    df_accounts = controller.load_accounts_per_period(*datetime_helpers.create_period(1))
    # df_accounts["Data"] = df_accounts["Data"].apply(helpers.format_data_br)
    st.dataframe(df_accounts, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)

    if col_registrar.button("➕ Registrar", key="register_account"):
        dialog_register.account_line()

    if col_deletar.button("❌ Deletar", key="delete_account"):
        dialog_delete.account_line()


def credit_card_screen():
    st.subheader("Cartões de Crédito")
    controller.create_credit_cards_table()
    df_credit_cards = controller.load_credit_cards_per_period(*datetime_helpers.create_period(1))
    # df_credit_cards["Data"] = df_credit_cards["Data"].apply(helpers.format_data_br)
    st.dataframe(df_credit_cards, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_credit_card"):
        dialog_register.credit_card_line()

    if col_deletar.button("❌ Deletar", key="delete_credit_card"):
        dialog_delete.credit_card_line()
        