import streamlit as st
import datetime
import locale
import data


locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def menu():
    st.sidebar.page_link("pages/dashboard.py", label="Gráficos", icon="📊")
    st.sidebar.page_link("pages/reports.py", label="Relatórios", icon="📄")
    st.sidebar.page_link("pages/settings.py", label="Configurações", icon="⚙️")


@st.experimental_dialog("Registrar Transação")
def dialog_register_transaction():
    data.Transaction.add_transaction()

@st.experimental_dialog("Registrar Categoria")
def dialog_register_categorie():
    data.Categorie.add_categorie()


@st.experimental_dialog("Registrar Conta")
def dialog_register_account():
    data.Account.add_account()


@st.experimental_dialog("Registrar Cartão de Crédito")
def dialog_register_credit_card():
    data.CreditCard.add_credit_card()


def format_data_br(data):
    if isinstance(data, str):
        formato = "%Y-%m-%d"
        formato_br = "%d/%m/%Y"
        data_datetime = datetime.datetime.strptime(data, formato)
        data_str = data_datetime.strftime(formato_br)
        return data_str
    
@st.experimental_dialog("Excluir transação", width="large")
def dialog_delete_transaction_line():
    df = data.loader.local_transactions()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        data.saver.local_transaction(df_result)
        st.rerun()
    

@st.experimental_dialog("Excluir categoria", width="large")
def dialog_delete_categorie_line():
    df = data.loader.local_categories()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        data.saver.local_categorie(df_result)
        st.rerun()


@st.experimental_dialog("Excluir conta", width="large")
def dialog_delete_account_line():
    df = data.loader.local_accounts()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        data.saver.local_account(df_result)
        st.rerun()


@st.experimental_dialog("Excluir cartão de crédito", width="large")
def dialog_delete_credit_card_line():
    df = data.loader.local_credit_cards()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        data.saver.local_credit_card(df_result)
        st.rerun()