import streamlit as st
from database import controller
from utils import datetime_helpers


@st.dialog("Excluir transação", width="large")
def transaction_line():
    df = controller.load_transactions_per_period(*datetime_helpers.create_period(1))

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        # saver.local_transaction(df_result)
        st.rerun()


@st.dialog("Excluir categoria", width="large")
def categorie_line():
    df = controller.load_categories_per_period(*datetime_helpers.create_period(1))

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        # saver.local_categorie(df_result)
        st.rerun()


@st.dialog("Excluir conta", width="large")
def account_line():
    df = controller.load_accounts_per_period(*datetime_helpers.create_period(1))

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        # saver.local_account(df_result)
        st.rerun()


@st.dialog("Excluir Cartão", width="large")
def credit_card_line():
    df = controller.load_credit_cards_per_period(*datetime_helpers.create_period(1))

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        # saver.local_credit_card(df_result)
        st.rerun()
        