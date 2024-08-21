import streamlit as st
from data import controller
from utils import helpers


@st.dialog("Registrar Transação")
def dialog_register_transaction():
    controller.Transaction.add_transaction()


@st.dialog("Excluir transação", width="large")
def dialog_delete_transaction_line():
    df = controller.load_transactions_per_period(controller.create_period(1))

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        st.rerun()


def transactions_screen():
    st.subheader("Transações")
    df_transactions = controller.load_transactions_per_period(*controller.create_period(1))
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
            df_categories = controller.load_categories_per_period(controller.create_period(1))
            df_accounts = controller.load_accounts_per_period(controller.create_period(1))
            df_credit_cards = controller.load_credit_cards_per_period(controller.create_period(1))

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
        controller.insert_transactions_rows(transaction.dataframe)
        st.rerun()