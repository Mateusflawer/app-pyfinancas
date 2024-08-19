    
from data import controller, loader, saver
from utils import helpers
import streamlit as st


@st.dialog("Registrar Categoria")
def dialog_register_categorie():
    controller.Categorie.add_categorie()


@st.dialog("Excluir categoria", width="large")
def dialog_delete_categorie_line():
    df = loader.local_categories()

    if not "Excluir" in df.columns:
        df.insert(0, "Excluir", False)

    df_result = st.data_editor(df, use_container_width=True, hide_index=True)
    
    if st.button("Excluir"):
        df_result = df_result[df_result["Excluir"]!=True]
        df_result = df_result.drop(columns=["Excluir"])
        saver.local_categorie(df_result)
        st.rerun()


def categories_screen():
    st.subheader("Categorias")
    df_categories = loader.local_categories()
    df_categories["Data"] = df_categories["Data"].apply(helpers.format_data_br)
    st.dataframe(df_categories, hide_index=True, use_container_width=True)
    col_registrar, col_deletar, col_editar = st.columns(3)
    
    if col_registrar.button("➕ Registrar", key="register_categorie"):
        dialog_register_categorie()

    if col_deletar.button("❌ Deletar", key="delete_categorie"):
        dialog_delete_categorie_line()


def add_categorie():
    categorie = controller.Categorie()
    categorie.nome = st.text_input("Nome")
    categorie.tipo = st.selectbox("Tipo", controller.TIPOS)

    categorie.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

    if st.button("Salvar"):
        controller.saver_local_categorie(categorie)
        st.rerun()