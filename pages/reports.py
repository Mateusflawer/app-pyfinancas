import streamlit as st
from utils import helpers
from data import loader

st.set_page_config("Relatórios", "📄", "wide",)

def main():
    helpers.menu()

    st.title("Bem vindo aos Relatórios!")

    df_transactions = loader.local_transactions()
    df_categories = loader.local_categories()
    df_accounts = loader.local_accounts()
    df_credit_cards = loader.local_credit_cards()

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Transações")
            st.dataframe(df_transactions, hide_index=True, use_container_width=True)
            if st.button("Registrar Transação", type="primary"):
                helpers.dialog_register_transaction()
        
        with st.container(border=True):
            st.subheader("Categorias")
            st.dataframe(df_categories, hide_index=True, use_container_width=True)
            if st.button("Registrar Categoria", type="primary"):
                helpers.dialog_register_categorie()

    with col2:
        with st.container(border=True):
            st.subheader("Contas")
            st.dataframe(df_accounts, hide_index=True, use_container_width=True)
            if st.button("Registrar Conta", type="primary"):
                helpers.dialog_register_account()
    
        with st.container(border=True):
            st.subheader("Cartões de Crédito")
            st.dataframe(df_credit_cards, hide_index=True, use_container_width=True)
            if st.button("Registrar Cartão de Crédito", type="primary"):
                helpers.dialog_register_credit_card()

if __name__ == "__main__":
    main()