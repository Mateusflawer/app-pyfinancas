from database import creator, loader, saver, delete
from pathlib import Path
import streamlit as st
import pandas as pd
import datetime
import locale

locale.setlocale(locale.LC_ALL, "")

ROOT_DIR = Path(__file__).parent.parent

ENTRADA = "Entrada"
DESPESA = "Despesa"

TIPOS = (ENTRADA, DESPESA)

TRANSACTIONS = "transactions"
ACCOUNTS = "accounts"
CATEGORIES = "categories"
CREDIT_CARDS = "credit_cards"

# Caminhos de arquivos
def check_empty_df(*args) -> bool:
    """Retorna VERDADEIRO se algum df estiver vazio"""
    df_empty = False

    # Loop
    for df in args:
        if df is None or df.empty:
            df_empty = True

    return df_empty


def create_transactions_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {TRANSACTIONS} (
        id INTEGER PRIMARY KEY, 
        data DATETIME, 
        categoria TEXT, 
        tipo TEXT, 
        conta TEXT, 
        cartao TEXT, 
        valor FLOAT, 
        descricao TEXT, 
        efetivada TEXT 
    )
    """
    creator.create_table(query)
    
    
def create_categories_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {CATEGORIES} (
        id INTEGER PRIMARY KEY, 
        data DATETIME, 
        nome TEXT, 
        tipo TEXT
    )
    """
    creator.create_table(query)
    
    
def create_accounts_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {ACCOUNTS} (
        id INTEGER PRIMARY KEY,
        data DATETIME, 
        nome TEXT
    )
    """
    creator.create_table(query)
    
    
def create_credit_cards_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {CREDIT_CARDS} (
        id INTEGER PRIMARY KEY, 
        data DATETIME, 
        nome TEXT, 
        fechamento DATETIME, 
        vencimento DATETIME, 
        limite FLOAT
    )
    """
    creator.create_table(query)


def load_transactions_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler as transações por período"""
    df = loader.load_per_period(TRANSACTIONS, start_date, end_date)
    return df


def load_categories_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler as categorias por período"""
    df = loader.load_per_period(CATEGORIES, start_date, end_date)
    return df


def load_accounts_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler as contas por período"""
    df = loader.load_per_period(ACCOUNTS, start_date, end_date)
    return df


def load_credit_cards_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler os cartões por período"""
    df = loader.load_per_period(CREDIT_CARDS, start_date, end_date)
    return df


def insert_transactions_rows(df: pd.DataFrame):
    saver.insert_rows(TRANSACTIONS, df)
    
    
def insert_categories_rows(df: pd.DataFrame):
    saver.insert_rows(CATEGORIES, df)
    
    
def insert_accounts_rows(df: pd.DataFrame):
    saver.insert_rows(ACCOUNTS, df)
    
    
def insert_credit_cards_rows(df: pd.DataFrame):
    saver.insert_rows(CREDIT_CARDS, df)


def load_nome_categories_by_tipo(tipo: str):
    df = loader.load_nome_by_tipo(CATEGORIES, tipo)
    return df


def load_nome_accounts():
    df = loader.load_nome(ACCOUNTS)
    return df


def load_nome_credit_cards():
    df = loader.load_nome(CREDIT_CARDS)
    return df


def delete_rows_transactions_by_id(ids: list):
    delete.delete_rows_by_id(TRANSACTIONS, ids)
    
    
def delete_rows_categories_by_id(ids: list):
    delete.delete_rows_by_id(CATEGORIES, ids)
    
    
def delete_rows_accounts_by_id(ids: list):
    delete.delete_rows_by_id(ACCOUNTS, ids)
    
    
def delete_rows_credit_cards_by_id(ids: list):
    delete.delete_rows_by_id(CREDIT_CARDS, ids)


if __name__ == "__main__":
    create_transactions_table()
    