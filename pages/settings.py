import streamlit as st
from utils import helpers

def main():
    helpers.menu()

    st.title("Bem vindo as Configurações!")
    st.info("Em desenvolvimento...", icon="⚙️")

if __name__ == "__main__":
    main()