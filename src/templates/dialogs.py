import streamlit as st
from database import controller
from handlers import processing
from utils import dataframe_helpers

tipos = controller.TIPOS

@st.dialog("Registrar Transação")
def register_transaction():
    with st.container(height=400):
        tipo = 'Entrada'
        
        descricao = st.text_area("Descrição")
        valor = st.number_input("Valor")
        lancamento = st.date_input("Laçamento", format="DD/MM/YYYY")
        vencimento = st.date_input("Vencimento", format="DD/MM/YYYY")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            if efetivado := col1.toggle('Efetivado', value=True):
                efetivacao = col2.date_input(
                    "Efetivação", format="DD/MM/YYYY", label_visibility='collapsed',
                    help='Data de efetivação!'
                )
        categories = controller.load_nome_categories_by_tipo(tipo)
        categoria = st.selectbox("Categoria", categories)
        subcategorias = []
        categoria = st.selectbox("Subcategorias", subcategorias, disabled=True)
        cartoes = []
        cartao = st.selectbox('Cartão', cartoes)
        accounts = controller.load_nome_accounts()
        conta = st.selectbox("Conta", accounts)

    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        controller.insert_transactions_rows(transaction.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
        

@st.dialog("Registrar Categoria")
def register_categorie():
    categorie = processing.Categorie()
    categorie.nome = st.text_input("Nome")
    categorie.tipo = st.selectbox("Tipo", controller.TIPOS)
    categorie.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)
    
    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        controller.insert_categories_rows(categorie.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.dialog("Registrar Conta")
def register_account():
    account = processing.Account()
    account.nome = st.text_input("Nome")
    account.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        controller.insert_accounts_rows(account.dataframe)
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.dialog("Excluir transação", width="large")
def delete_transaction():
    df = controller.load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )
    
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
    
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df = st.data_editor(df, use_container_width=True, hide_index=True)
    
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        df = df[df["Excluir"]==True]
        ids = df["id"].tolist()
        controller.delete_rows_transactions_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.dialog("Excluir categoria", width="large")
def delete_categorie():
    df = controller.load_categories()
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
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
        st.rerun()

@st.dialog("Excluir conta", width="large")
def delete_account():
    df = controller.load_accounts()
    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)
        
        if not dataframe_helpers.check_empty_df(df):
            df = df.copy()
            
    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        df_result = df_result[df_result["Excluir"]==True]
        ids = df_result["id"].tolist()
        controller.delete_rows_accounts_by_id(ids)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
