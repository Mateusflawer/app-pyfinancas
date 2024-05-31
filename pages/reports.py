import streamlit as st
from utils import helpers
from data import loader, controller

st.set_page_config("Relatórios", "📄", "wide",)

def main():
    helpers.menu()

    st.title("Bem vindo aos Relatórios!")

    # Sempre checar se os arquvos dos dados existem antes de carrega-los
    controller.check_data()

    # Carregando dados após checar que existem os arquivos
    df_transactions = loader.local_transactions()
    df_categories = loader.local_categories()
    df_accounts = loader.local_accounts()
    df_credit_cards = loader.local_credit_cards()

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Transações")
            df_transactions["Data"] = df_transactions["Data"].apply(helpers.format_data_br)
            st.dataframe(df_transactions, hide_index=True, use_container_width=True)
            col_registrar, col_deletar, col_editar = st.columns(3)
            if col_registrar.button("Registrar Transação", type="primary"):
                helpers.dialog_register_transaction()

            if col_deletar.button("Deletar Transação", type="primary"):
                helpers.dialog_delete_transaction_line()
        
        with st.container(border=True):
            st.subheader("Categorias")
            df_categories["Data"] = df_categories["Data"].apply(helpers.format_data_br)
            st.dataframe(df_categories, hide_index=True, use_container_width=True)
            if st.button("Registrar Categoria", type="primary"):
                helpers.dialog_register_categorie()

    with col2:
        with st.container(border=True):
            st.subheader("Contas")
            df_accounts["Data"] = df_accounts["Data"].apply(helpers.format_data_br)
            st.dataframe(df_accounts, hide_index=True, use_container_width=True)
            if st.button("Registrar Conta", type="primary"):
                helpers.dialog_register_account()
    
        with st.container(border=True):
            st.subheader("Cartões de Crédito")
            df_credit_cards["Data"] = df_credit_cards["Data"].apply(helpers.format_data_br)
            st.dataframe(df_credit_cards, hide_index=True, use_container_width=True)
            if st.button("Registrar Cartão de Crédito", type="primary"):
                helpers.dialog_register_credit_card()

if __name__ == "__main__":
    main()