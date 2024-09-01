import streamlit as st
from database import controller
from utils import datetime_helpers


@st.dialog("Excluir transação", width="large")
def transaction_line():
    df = controller.load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    col_excluir, col_cancelar = st.columns(2)
    
    if col_excluir.button("Excluir ✅"):
        df_result = df_result[df_result["Excluir"]==True]
        ids = df_result["id"].tolist()
        controller.delete_rows_transactions_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.cache_resource.clear()
        st.rerun()


@st.dialog("Excluir categoria", width="large")
def categorie_line():
    df = controller.load_categories()

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
        st.cache_resource.clear()
        st.rerun()


@st.dialog("Excluir conta", width="large")
def account_line():
    df = controller.load_accounts()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    col_excluir, col_cancelar = st.columns(2)
    
    if col_excluir.button("Excluir ✅"):
        df_result = df_result[df_result["Excluir"]==True]
        ids = df_result["id"].tolist()
        controller.delete_rows_accounts_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.cache_resource.clear()
        st.rerun()


@st.dialog("Excluir Cartão", width="large")
def credit_card_line():
    df = controller.load_credit_cards()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    col_excluir, col_cancelar = st.columns(2)
    
    if col_excluir.button("Excluir ✅"):
        df_result = df_result[df_result["Excluir"]==True]
        ids = df_result["id"].tolist()
        controller.delete_rows_credit_cards_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.cache_resource.clear()
        st.rerun()
        