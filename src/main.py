import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "")

def main():
    st.switch_page("pages\\0_login.py")    

if __name__ == "__main__":
    main()
