import streamlit as st
import utils
import data
import utils
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

st.set_page_config("Relatórios", "📄", "wide",)

def transactions_screen():
    st.subheader("Transações")
    df_transactions = data.loader.local_transactions()
    df_transactions["Data"] = df_transactions["Data"].apply(utils.helpers.format_data_br)
    st.dataframe(df_transactions, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_transaction"):
        utils.helpers.dialog_register_transaction()

    if col_deletar.button("❌ Deletar", key="delete_transaction"):
        utils.helpers.dialog_delete_transaction_line()

def categories_screen():
    st.subheader("Categorias")
    df_categories = data.loader.local_categories()
    df_categories["Data"] = df_categories["Data"].apply(utils.helpers.format_data_br)
    st.dataframe(df_categories, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_categorie"):
        utils.helpers.dialog_register_categorie()

    if col_deletar.button("❌ Deletar", key="delete_categorie"):
        utils.helpers.dialog_delete_categorie_line()
            
def accounts_screen():
    st.subheader("Contas")
    df_accounts = data.loader.local_accounts()
    df_accounts["Data"] = df_accounts["Data"].apply(utils.helpers.format_data_br)
    st.dataframe(df_accounts, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)

    if col_registrar.button("➕ Registrar", key="register_account"):
        utils.helpers.dialog_register_account()

    if col_deletar.button("❌ Deletar", key="delete_account"):
        utils.helpers.dialog_delete_account_line()

def credit_card_screen():
    st.subheader("Cartões de Crédito")
    df_credit_cards = data.loader.local_credit_cards()
    df_credit_cards["Data"] = df_credit_cards["Data"].apply(utils.helpers.format_data_br)
    st.dataframe(df_credit_cards, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_credit_card"):
        utils.helpers.dialog_register_credit_card()

    if col_deletar.button("❌ Deletar", key="delete_credit_card"):
        utils.helpers.dialog_delete_credit_card_line()

def main():
    utils.helpers.menu()

    st.title("Bem vindo aos Relatórios!")

    # Sempre checar se os arquvos dos dados existem antes de carrega-los
    data.controller.check_data_all()

    # Carregando dados após checar que existem os arquivos
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True): 
            transactions_screen()

        with st.container(border=True): 
            categories_screen()

    with col2:
        with st.container(border=True): 
            accounts_screen()

        with st.container(border=True): 
            credit_card_screen()

if __name__ == "__main__":
    main()