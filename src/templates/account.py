import streamlit as st
from data import controller, loader, saver
from utils import helpers


@st.dialog("Registrar Conta")
def dialog_register_account():
    controller.Account.add_account()


@st.dialog("Excluir conta", width="large")
def dialog_delete_account_line():
    df = loader.local_accounts()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        saver.local_account(df_result)
        st.rerun()


def accounts_screen():
    st.subheader("Contas")
    df_accounts = loader.local_accounts()
    df_accounts["Data"] = df_accounts["Data"].apply(helpers.format_data_br)
    st.dataframe(df_accounts, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)

    if col_registrar.button("➕ Registrar", key="register_account"):
        dialog_register_account()

    if col_deletar.button("❌ Deletar", key="delete_account"):
        dialog_delete_account_line()


def add_account():
    account = controller.Account()
    account.nome = st.text_input("Nome")

    account.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    if st.button("Salvar"):
        controller.insert_accounts_rows(account.dataframe)
        st.rerun()