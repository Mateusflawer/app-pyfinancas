import streamlit as st
from data import controller
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def main():

    controller.loader_transactions()
    controller.loader_categories()
    controller.loader_accounts()
    controller.loader_credit_cards()

    st.switch_page("pages/dashboard.py")    

if __name__ == "__main__":
    main()
