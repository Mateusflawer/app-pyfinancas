import streamlit as st
from data import controller, loader, saver
from utils import helpers


@st.dialog("Registrar Transação")
def dialog_register_transaction():
    controller.Transaction.add_transaction()


@st.dialog("Excluir transação", width="large")
def dialog_delete_transaction_line():
    df = loader.local_transactions()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        saver.local_transaction(df_result)
        st.rerun()


def transactions_screen():
    st.subheader("Transações")
    df_transactions = loader.local_transactions()
    df_transactions["Data"] = df_transactions["Data"].apply(helpers.format_data_br)
    st.dataframe(df_transactions, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_transaction"):
        dialog_register_transaction()

    if col_deletar.button("❌ Deletar", key="delete_transaction"):
        dialog_delete_transaction_line()


def add_transation():
    with st.container(height=400):
        with st.spinner("Carregando dados..."):
            df_categories = loader.local_categories()
            df_accounts = loader.local_accounts()
            df_credit_cards = loader.local_credit_cards()

        transaction = controller.Transaction()

        transaction.descricao = st.text_area("Descrição")

        credito = st.toggle("Crédito?")

        if not credito:
            transaction.tipo = st.selectbox("Tipo", controller.TIPOS)
        else:
            transaction.tipo = controller.TIPOS[1] # Despesa
        
        if transaction.tipo == controller.TIPOS[0]: # Se entrada
            categorias = df_categories[df_categories["Tipo"]==controller.TIPOS[0]]["Nome"].unique()
        else:
            categorias = df_categories[df_categories["Tipo"]==controller.TIPOS[1]]["Nome"].unique()

        transaction.categoria = st.selectbox("Categoria", categorias)
    
        if credito:
            transaction.credit_card = st.selectbox("Cartão de crédito", df_credit_cards["Nome"].unique())
        else:
            transaction.conta = st.selectbox("Conta", df_accounts["Nome"].unique())

        transaction.data = st.date_input("Data", format="DD/MM/YYYY")
        transaction.valor = st.number_input("Valor")

    if st.button("Salvar"):
        controller.saver_local_transaction(transaction)
        st.rerun()