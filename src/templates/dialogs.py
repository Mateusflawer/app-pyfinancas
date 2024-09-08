import streamlit as st
from database import controller
from handlers import processing
from utils import dataframe_helpers

TIPOS = ['Entrada', 'Saida']


@st.fragment()
@st.dialog("Registrar Transação")
def register_transaction():
    with st.container(height=400):
        transaction = processing.Transaction()
        transaction.tipo = st.selectbox('Tipo', TIPOS)
        transaction.descricao = st.text_area("Descrição")
        transaction.valor = st.number_input("Valor")
        transaction.lancamento = st.date_input("Laçamento", format="DD/MM/YYYY")
        transaction.vencimento = st.date_input("Vencimento", format="DD/MM/YYYY")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            if efetivado := col1.toggle('Efetivado', value=True):
                transaction.efetivacao = col2.date_input(
                    "Efetivação", format="DD/MM/YYYY", label_visibility='collapsed',
                    help='Data de efetivação!'
                )
        categories = controller.load_nome_categories_by_tipo(transaction.tipo)
        transaction.categoria = st.selectbox("Categoria", categories)
        subcategorias = []
        transaction.subcategoria = st.selectbox("Subcategorias", subcategorias)
        cartoes = []
        transaction.cartao = st.selectbox('Cartão', cartoes)
        accounts = controller.load_nome_accounts()
        transaction.conta = st.selectbox("Conta", accounts)

    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        controller.insert_transactions_rows(transaction.get_df())
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
        
        
@st.fragment()
@st.dialog("Registrar Categoria")
def register_categorie():
    categorie = processing.Categorie()
    categorie.nome = st.text_input("Nome")
    categorie.tipo = st.selectbox("Tipo", TIPOS)
    categorie.lancamento = st.date_input("Lançamento", format="DD/MM/YYYY", disabled=True)
    
    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        controller.insert_categories_rows(categorie.get_df())
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog("Registrar Conta")
def register_account():
    account = processing.Account()
    account.nome = st.text_input("Nome")
    account.lancamento = st.date_input("Lançamento", format="DD/MM/YYYY", disabled=True)

    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        controller.insert_accounts_rows(account.get_df())
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


################################################################################


@st.fragment()
@st.dialog('Editar Transação', width='small')
def edit_transaction():
    st.info('Em desenvolvimento...', icon='⚙️')
    
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog('Editar Categoria', width='small')
def edit_categorie():
    st.info('Em desenvolvimento...', icon='⚙️')
    
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog('Editar Conta', width='small')
def edit_account():
    st.info('Em desenvolvimento...', icon='⚙️')
    
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()

################################################################################


@st.fragment()
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
            
    df_editado = st.data_editor(
        df, 
        use_container_width=True, hide_index=True
    )
    
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        controller.delete_rows_transactions_by_id(df_editado)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog("Excluir categoria", width="large")
def delete_categorie():
    df = controller.load_categories()
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
        
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df_editado = st.data_editor(
        df, 
        use_container_width=True, hide_index=True
    )
    col_excluir, col_cancelar = st.columns(2)
    
    if col_excluir.button("Excluir ✅"):
        controller.delete_rows_categories_by_id(df_editado)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog("Excluir conta", width="large")
def delete_account():
    df = controller.load_accounts()
        
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
        
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df_editado = st.data_editor(
        df, 
        use_container_width=True, hide_index=True
    )
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        controller.delete_rows_accounts_by_id(df_editado)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
        