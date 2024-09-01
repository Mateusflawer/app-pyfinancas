import streamlit as st
import sqlite3
from .config import (
    DATABASE, TRANSACTIONS, CATEGORIES, ACCOUNTS, CREDIT_CARDS
)

def delete_rows_by_id(table: str, ids: list):
    """
    Deleta linhas de uma tabela com base nos IDs fornecidos.

    :param table: Nome da tabela onde as linhas serão deletadas.
    :param ids: Lista de IDs das linhas a serem deletadas.
    :param database: Caminho para o arquivo do banco de dados SQLite.
    """
    # Conecte-se ao banco de dados
    conn = sqlite3.connect(DATABASE)

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Prepare a consulta SQL para deletar linhas com base no id
    sql = f"DELETE FROM {table} WHERE id = ?"

    # Deleta cada linha correspondente a um id na lista de ids
    for id in ids:
        cursor.execute(sql, (id,))

    # Confirmar alterações
    conn.commit()

    # Feche a conexão
    cursor.close()
    conn.close()


def delete_rows_transactions_by_id(ids: list):
    delete_rows_by_id(TRANSACTIONS, ids)
    st.cache_resource.clear()
    
    
def delete_rows_categories_by_id(ids: list):
    delete_rows_by_id(CATEGORIES, ids)
    st.cache_resource.clear()
    
    
def delete_rows_accounts_by_id(ids: list):
    delete_rows_by_id(ACCOUNTS, ids)
    st.cache_resource.clear()
    
    
def delete_rows_credit_cards_by_id(ids: list):
    delete_rows_by_id(CREDIT_CARDS, ids)
    st.cache_resource.clear()