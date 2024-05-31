from data import controller, loader, saver
import streamlit as st
import datetime
import locale

TIPOS =  ("Entradas", "Despesas")

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def menu():
    st.sidebar.page_link("pages/dashboard.py", label="Gráficos", icon="📊")
    st.sidebar.page_link("pages/reports.py", label="Relatórios", icon="📄")
    st.sidebar.page_link("pages/settings.py", label="Configurações", icon="⚙️")


@st.experimental_dialog("Registrar Transação")
def dialog_register_transaction():

    with st.spinner("Carregando dados..."):
        df_categories = loader.local_categories()
        df_accounts = loader.local_accounts()
        df_credit_cards = loader.local_credit_cards()

    transaction = controller.Transaction()

    transaction.descricao = st.text_area("Descrição")

    transaction.tipo = st.selectbox("Tipo", TIPOS)
    
    if transaction.tipo == "Entradas":
        categorias = df_categories[df_categories["Tipo"]=="Entradas"]["Nome"].unique()
    else:
        categorias = df_categories[df_categories["Tipo"]=="Despesas"]["Nome"].unique()

    transaction.categoria = st.selectbox("Categoria", categorias)
    credito = st.toggle("Crédito?")
    if credito:
        transaction.credit_card = st.selectbox("Cartão de crédito", df_credit_cards["Nome"].unique())
    else:
        transaction.conta = st.selectbox("Conta", df_accounts["Nome"].unique())

    transaction.data = st.date_input("Data", format="DD/MM/YYYY")
    transaction.valor = st.number_input("Valor")

    if st.button("Salvar"):
        controller.saver_local_transaction(transaction)
        st.rerun()

@st.experimental_dialog("Registrar Categoria")
def dialog_register_categorie():

    categorie = controller.Categorie()
    categorie.nome = st.text_input("Nome")
    categorie.tipo = st.selectbox("Tipo", TIPOS)

    categorie.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    if st.button("Salvar"):
        controller.saver_local_categorie(categorie)
        st.rerun()


@st.experimental_dialog("Registrar Conta")
def dialog_register_account():

    account = controller.Account()
    account.nome = st.text_input("Nome")

    account.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    if st.button("Salvar"):
        controller.saver_local_account(account)
        st.rerun()


@st.experimental_dialog("Registrar Cartão de Crédito")
def dialog_register_credit_card():

    credit_card = controller.CreditCard()
    credit_card.nome = st.text_input("Nome")

    credit_card.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    credit_card.fechamento = st.number_input("Fechamento", step=0, min_value=1, max_value=31)
    credit_card.vencimento = st.number_input("Vencimento", step=0, min_value=1, max_value=31)
    credit_card.limite = st.number_input("Limite", step=10)

    if st.button("Salvar"):
        controller.saver_local_credit_card(credit_card)
        st.rerun()


def format_data_br(data):
    if isinstance(data, str):
        formato = "%Y-%m-%d"
        formato_br = "%d/%m/%Y"
        data_datetime = datetime.datetime.strptime(data, formato)
        data_str = data_datetime.strftime(formato_br)
        return data_str
    
@st.experimental_dialog("Excluir transação")
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
    