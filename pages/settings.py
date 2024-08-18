import streamlit as st
from templates import sidebar
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def main():
    sidebar.menu()

    st.title("Bem vindo as Configurações!")
    st.info("Em desenvolvimento...", icon="⚙️")

if __name__ == "__main__":
    main()