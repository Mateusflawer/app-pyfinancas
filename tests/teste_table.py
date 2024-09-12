import streamlit as st
import pandas as pd

# Criar uma tabela de exemplo
# Criar um DataFrame de exemplo
df = pd.DataFrame({
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [20, 22, 25],
    'Nota': [8.5, 9.0, 7.5],
})

def tabela_dinamica(df: pd.DataFrame):
    # Criar cabeçalho
    st.markdown("<div style='overflow-x: auto'>", unsafe_allow_html=True)
    with st.container(border=True, height=500):
        cols_header = st.columns(len(df.columns))
        for i, col in enumerate(df.columns):
            cols_header[i].markdown(f':blue[{col}]')

        # Criar valores das colunas
        for _, row in df.iterrows():
            cols = st.columns(len(df.columns))
            for i, col in enumerate(df.columns):
                cols[i].markdown(row[col])
    st.markdown("</div>", unsafe_allow_html=True)
                
tabela_dinamica(df)