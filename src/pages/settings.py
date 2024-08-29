from utils import autenticated_helpers
from templates import sidebar
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "")

def main():
    sidebar.menu()

    st.toast("Em desenvolvimento...", icon="⚙️")

if __name__ == "__main__":
    if autenticated_helpers.autenticated():
        # Configurações da página
        st.set_page_config("Configurações", "⚙️", "wide")
        main()
    else:
        st.switch_page("pages/login.py")
        