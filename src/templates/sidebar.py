import streamlit as st
from datetime import datetime
from database import controller
import calendar

def menu():
    with st.sidebar:
        st.header("Py Finanças", divider=True)
        st.page_link("pages/dashboard.py", label="Gráficos", icon="📊")
        st.page_link("pages/reports.py", label="Relatórios", icon="📄")
        st.page_link("pages/settings.py", label="Configurações", icon="⚙️")
        st.divider()
        
        # Supondo que controller já tenha as funções definidas
        df_anos = controller.load_years_transactions()
        lista_de_anos = df_anos["ano"].tolist()
        ano_selected = st.selectbox("Ano", lista_de_anos)

        df_meses = controller.load_months_transactions_by_year(ano_selected)
        lista_de_meses = df_meses["mes"].tolist()

        # Converte os números dos meses para nomes completos
        lista_de_meses_nome = [calendar.month_name[int(mes)] for mes in lista_de_meses]

        # Seleciona os nomes dos meses
        meses_nome_selected = st.multiselect("Meses", lista_de_meses_nome, lista_de_meses_nome)

        # Converte os nomes dos meses selecionados para números
        meses_selected = [str(list(calendar.month_name).index(mes_nome)).zfill(2) for mes_nome in meses_nome_selected]

        st.session_state["ano_selected"] = ano_selected
        st.session_state["meses_selected"] = meses_selected
        