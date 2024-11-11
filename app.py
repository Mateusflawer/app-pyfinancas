import streamlit as st
from utils import instalador
import locale

locale.setlocale(locale.LC_ALL, "")


# Chamar a função para instalar os pacotes
def main():
    instalador.install_requirements()
    st.switch_page("pages/0_login.py")


if __name__ == "__main__":
    main()
