from pathlib import Path
import streamlit as st
import pandas as pd
import sqlite3

ROOT_DIR = Path(__file__).parent.parent

DATABASE = ROOT_DIR / "database" / "database.db"


def load_data(table: str):
    conn = sqlite3.connect(DATABASE)
    
    query = f"""
        SELECT * FROM {table} WHERE user_id = ?
    """
    
    params = (st.session_state["user_id"],)
    
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def load_nome_by_tipo(table:str, tipo: str) -> pd.DataFrame:
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table}
        WHERE tipo = ? AND user_id = ?  
        GROUP BY nome
    """
    
    params = (tipo, st.session_state["user_id"])
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_nome(table: str):
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table} 
        WHERE user_id = ? 
        GROUP BY nome
    """
    params = (st.session_state["user_id"],)
    df = pd.read_sql_query(query, conn, params=params)

    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_years(table: str):
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT DISTINCT 
            strftime('%Y', data) AS ano 
        FROM {table} 
        WHERE user_id = ? 
        ORDER BY ano DESC
    """
    params = (st.session_state["user_id"],)
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_months_by_year(table: str, year: str):
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT DISTINCT 
            strftime('%m', data) AS mes 
        FROM {table} 
        WHERE strftime('%Y', data) = ? AND user_id = ? 
        ORDER BY mes DESC
    """
    params = (year, st.session_state["user_id"])
    
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_data_by_year_and_selected_months(table: str, selected_year: str, months: list):
    conn = sqlite3.connect(DATABASE)
    
    # Construa a cláusula IN para os meses
    placeholders = ', '.join('?' for _ in months)
    
    query = f"""
        SELECT * 
        FROM {table}
        WHERE strftime('%Y', data) = ? 
        AND strftime('%m', data) IN ({placeholders}) 
        AND user_id = ? 
        ORDER BY strftime('%Y', data), strftime('%m', data) DESC
    """
    
    # Parâmetros combinados (ano, meses e user_id)
    params = (selected_year, *months, st.session_state["user_id"])
    
    # Execute a consulta SQL
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()
    return df


def load_credentials(table: str, username: str, password: str) -> pd.DataFrame:
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT 
            * 
        FROM {table} 
        WHERE ? = username AND ? = password 
    """

    params = (username, password)

    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()
    return df


if __name__ == "__main__":
    # df_years = load_years("transactions")
    # df_months = load_months_by_year("transactions", '2024')
    # df = load_data_by_year_and_selected_months('transactions', '2024', ['06', '07', '08'])
    # print(df_years)
    # print(df_months)
    # print(df)
    
    df = load_credentials("users", "mateus", "123")
    print(df)