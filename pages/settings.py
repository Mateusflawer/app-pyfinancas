import streamlit as st
import utils
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def main():
    utils.helpers.menu()

    st.title("Bem vindo as Configurações!")
    st.info("Em desenvolvimento...", icon="⚙️")

if __name__ == "__main__":
    main()