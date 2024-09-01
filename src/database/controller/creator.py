import sqlite3
from .config import (
    DATABASE, TRANSACTIONS, CATEGORIES, ACCOUNTS, USERS
)

def create_table(query: str):
    # Conecte-se ao banco de dados (ou crie um novo se não existir)
    conn = sqlite3.connect(DATABASE)

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Crie uma tabela
    cursor.execute(query)

    # Confirmar alterações
    conn.commit()

    # Feche a conexão
    cursor.close()
    conn.close()


def create_transactions_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {TRANSACTIONS} (
        id INTEGER PRIMARY KEY, 
        user_id INT, 
        data DATETIME, 
        categoria TEXT, 
        tipo TEXT, 
        conta TEXT, 
        valor FLOAT, 
        descricao TEXT, 
        efetivada TEXT 
    )
    """
    create_table(query)
    
    
def create_categories_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {CATEGORIES} (
        id INTEGER PRIMARY KEY, 
        user_id INT, 
        data DATETIME, 
        nome TEXT, 
        tipo TEXT
    )
    """
    create_table(query)
    
    
def create_accounts_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {ACCOUNTS} (
        id INTEGER PRIMARY KEY, 
        user_id INT, 
        data DATETIME, 
        nome TEXT
    )
    """
    create_table(query)


def create_users_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {USERS} (
        id INTEGER PRIMARY KEY, 
        username TEXT, 
        password TEXT, 
        email TEXT, 
        data DATETIME 
    )
    """
    create_table(query)