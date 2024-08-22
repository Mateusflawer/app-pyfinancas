from database import creator, loader, saver
from pathlib import Path
import pandas as pd
import datetime
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

ROOT_DIR = Path(__file__).parent.parent

ENTRADA = "Entrada"
DESPESA = "Despesa"

TIPOS = (ENTRADA, DESPESA)


class Transaction:
    def __init__(self):
        self._data = None
        self.descricao = None
        self.categoria = None
        self.tipo = None
        self.conta = None
        self.cartao = None
        self.valor = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._data, "%Y-%m-%d")
        return data_hora

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def dataframe(self):
        data = [{
            "data": self._data,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "tipo": self.tipo,
            "conta": self.conta,
            "cartao": self.cartao,
            "valor": self.valor,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_transaction(cls):
        pass


class Categorie:
    def __init__(self):
        self.nome = None
        self._data = None
        self.tipo = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._data, "%Y-%m-%d")
        return data_hora

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def dataframe(self):
        data = [{
            "data": self._data,
            "nome": self.nome,
            "tipo": self.tipo,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_categorie(cls):
        pass
    

class Account:
    def __init__(self):
        self.nome = None
        self._data = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._data, "%Y-%m-%d %H:%M:%S")
        return data_hora

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def dataframe(self):
        data = [{
            "data": self._data,
            "nome": self.nome,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_account(cls):
        pass
    

class CreditCard:
    def __init__(self):
        self.nome = None
        self._data = None
        self.fechamento = None
        self.vencimento = None
        self.limite = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._data, "%Y-%m-%d")
        return data_hora

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def dataframe(self):
        data = [{
            "data": self._data,
            "nome": self.nome,
            "fechamento": self.fechamento,
            "vencimento": self.vencimento,
            "limite": self.limite,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_credit_card(cls):
        pass


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
    creator.create_table(query)
    
    
def create_categories_table():
    query = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY, 
        data DATETIME, 
        nome TEXT, 
        tipo TEXT
    )
    """
    creator.create_table(query)
    
    
def create_accounts_table():
    query = """
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY,
        data DATETIME, 
        nome TEXT
    )
    """
    creator.create_table(query)
    
    
def create_credit_cards_table():
    query = """
    CREATE TABLE IF NOT EXISTS credit_cards (
        id INTEGER PRIMARY KEY, 
        data DATETIME, 
        nome TEXT, 
        fechamento DATETIME, 
        venvimento DATETIME, 
        limite FLOAT
    )
    """
    creator.create_table(query)


def load_transactions_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler as transações por período"""
    df = loader.load_per_period("transactions", start_date, end_date)
    return df


def load_categories_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler as categorias por período"""
    df = loader.load_per_period("categories", start_date, end_date)
    return df


def load_accounts_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler as contas por período"""
    df = loader.load_per_period("accounts", start_date, end_date)
    return df


def load_credit_cards_per_period(start_date: datetime, end_date: datetime) -> pd.DataFrame:
    """Ler os cartões por período"""
    df = loader.load_per_period("credit_cards", start_date, end_date)
    return df


def insert_transactions_rows(df: pd.DataFrame):
    saver.insert_rows("transactions", df)
    
    
def insert_categories_rows(df: pd.DataFrame):
    saver.insert_rows("categories", df)
    
    
def insert_accounts_rows(df: pd.DataFrame):
    saver.insert_rows("accounts", df)
    
    
def insert_credit_cards_rows(df: pd.DataFrame):
    saver.insert_rows("credit_cards", df)

if __name__ == "__main__":
    create_transactions_table()
    