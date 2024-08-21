import streamlit as st
import sqlite3
from pathlib import Path
import pandas as pd
import datetime

# PASTA DO PROJETO
ROOT_DIR = Path(__file__).parent.parent

DATA_DIR = ROOT_DIR / "src" / "data"
DATABASE = DATA_DIR / "database.db"

def creat_table(query: str):
    # Conecte-se ao banco de dados (ou crie um novo se não existir)
    conn = sqlite3.connect(DATABASE)

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Crie uma tabela
    cursor.execute(query)

    # cursor.execute("""
    # INSERT INTO transactions (data, categoria, tipo, conta, cartao, valor, descricao) 
    # VALUES ('data', 'c', 't', 'c', 'c', '1', 'd')
    # """)

    # Confirmar alterações
    conn.commit()

    # # Realize uma consulta
    # cursor.execute("SELECT * FROM transactions")

    # transactions = cursor.fetchall()
    # df = pd.DataFrame(transactions)
    # colunas = [description[0] for description in cursor.description]
    # df.columns = colunas
    # st.dataframe(df.infer_objects())

    # Feche a conexão
    cursor.close()
    conn.close()
    

if __name__ == "__main__":
    query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        data DATETIME, 
        categoria TEXT, 
        tipo TEXT, 
        conta TEXT, 
        cartao TEXT,
        valor FLOAT, 
        descricao TEXT
    )
    """
    creat_table(query)