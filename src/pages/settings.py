import streamlit as st
from templates import sidebar
import locale

locale.setlocale(locale.LC_ALL, "")

def main():
    sidebar.menu()

    st.toast("Em desenvolvimento...", icon="⚙️")

if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Configurações", "⚙️", "wide")
    main()