import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def main():
    st.switch_page("pages/dashboard.py")    

if __name__ == "__main__":
    main()
