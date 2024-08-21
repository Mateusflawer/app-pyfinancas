import streamlit as st
from data import controller, loader, saver
from utils import helpers

@st.dialog("Registrar Cartão de Crédito")
def dialog_register_credit_card():
    controller.CreditCard.add_credit_card()


@st.dialog("Excluir cartão de crédito", width="large")
def dialog_delete_credit_card_line():
    df = loader.local_credit_cards()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        saver.local_credit_card(df_result)
        st.rerun()


def credit_card_screen():
    st.subheader("Cartões de Crédito")
    df_credit_cards = loader.local_credit_cards()
    df_credit_cards["Data"] = df_credit_cards["Data"].apply(helpers.format_data_br)
    st.dataframe(df_credit_cards, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_credit_card"):
        dialog_register_credit_card()

    if col_deletar.button("❌ Deletar", key="delete_credit_card"):
        dialog_delete_credit_card_line()


def add_credit_card():
    credit_card = controller.CreditCard()
    credit_card.nome = st.text_input("Nome")

    credit_card.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    credit_card.fechamento = st.number_input("Fechamento", step=0, min_value=1, max_value=31)
    credit_card.vencimento = st.number_input("Vencimento", step=0, min_value=1, max_value=31)
    credit_card.limite = st.number_input("Limite", step=10)

    if st.button("Salvar"):
        controller.insert_credit_cards_rows(credit_card.dataframe)
        st.rerun()
        