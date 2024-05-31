import streamlit as st
import utils

def main():
    utils.helpers.menu()

    st.title("Bem vindo as Configurações!")
    st.info("Em desenvolvimento...", icon="⚙️")

if __name__ == "__main__":
    main()