from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import sqlite3

ROOT_DIR = Path(__file__).parent.parent

DATABASE = ROOT_DIR / "database" / "database.db"


def load_data(table: str):
    conn = sqlite3.connect(DATABASE)
    
    query = f"""
        SELECT * FROM {table}
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def load_nome_by_tipo(table:str, tipo: str) -> pd.DataFrame:
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table}
        WHERE tipo = ? GROUP BY nome
    """
    
    params = (tipo,)
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_nome(table: str):
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table} GROUP BY nome
    """
    
    df = pd.read_sql_query(query, conn)

    conn.close()  # Fechar a conexão após a execução da consulta
    return df



def load_years(table: str):
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT DISTINCT 
            strftime('%Y', data) AS ano 
        FROM {table} 
        ORDER BY ano DESC
    """
    
    df = pd.read_sql_query(query, conn)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_months_by_year(table: str, year: str):
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT DISTINCT 
            strftime('%m', data) AS mes 
        FROM {table} 
        WHERE strftime('%Y', data) = ?
        ORDER BY mes DESC
    """
    params = (year,)
    
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_data_by_year_and_selected_months(table: str, selected_year: str, months: list):
    conn = sqlite3.connect(DATABASE)

    # Converter a lista de meses em uma string formatada para a cláusula IN
    meses_str = ', '.join([f"'{mes}'" for mes in months])

    query = f"""
        SELECT * 
        FROM {table}
        WHERE strftime('%Y', data) = '{selected_year}'
        AND strftime('%m', data) IN ({meses_str})
        ORDER BY strftime('%Y', data), strftime('%m', data) DESC
    """
    
    df = pd.read_sql_query(query, conn)
    
    conn.close()
    return df


if __name__ == "__main__":
    df_years = load_years("transactions")
    df_months = load_months_by_year("transactions", '2024')
    df = load_data_by_year_and_selected_months('transactions', '2024', ['06', '07', '08'])
    print(df_years)
    print(df_months)
    print(df)