from templates import account, categorie, credit_card, transaction
import pandas as pd
import datetime
import locale
import data
import os

locale.setlocale(locale.LC_ALL, "portuguese_brazil")
TIPOS =  ("Entrada", "Despesa")

class Transaction:
    def __init__(self):
        self._data = None
        self.descricao = None
        self.categoria = None
        self.tipo = None
        self.conta = None
        self.credit_card = None
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
            "Data": self._data,
            "Descricao": self.descricao,
            "Categoria": self.categoria,
            "Tipo": self.tipo,
            "Conta": self.conta,
            "Cartão de Crédito": self.credit_card,
            "Valor": self.valor,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_transaction(cls):
        transaction.add_transation()

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
            "Data": self._data,
            "Nome": self.nome,
            "Tipo": self.tipo,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_categorie(cls):
        categorie.add_categorie()
    
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
            "Data": self._data,
            "Nome": self.nome,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_account(cls):
        account.add_account()
    
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
            "Data": self._data,
            "Nome": self.nome,
            "Fechamento": self.fechamento,
            "Vencimento": self.vencimento,
            "Limite": self.limite,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_credit_card(cls):
        credit_card.add_credit_card()

# Caminhos de arquivos
def check_empty_df(*args):
    """
    Retorna 'True' se tiver algum df vazio
    """
    df_empty = False

    for df in args:
        if df is None or df.empty:
            df_empty = True

    return df_empty

def check_transactions():
    if not os.path.exists(data.loader.LOCAL_TRANSACTIONS):
        data.creator.create_local_transactions()

def check_categories():
    if not os.path.exists(data.loader.LOCAL_CATEGORIES):
        data.creator.create_local_categories()

def check_accounts():
    if not os.path.exists(data.loader.LOCAL_ACCOUNTS):
        data.creator.create_local_accounts()

def check_credit_cards():
    if not os.path.exists(data.loader.LOCAL_CREDIT_CARDS):
        data.creator.create_local_credit_cards()

def check_data_all():
    check_accounts()
    check_categories()
    check_credit_cards()
    check_transactions()
        
def saver_local_transaction(transaction):
    try:
        df_transaction = data.loader.local_transactions()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_transaction, transaction.dataframe], ignore_index=True)

    data.saver.local_transaction(df_result)
    return True

def saver_local_categorie(categorie):
    try:
        df_categories = data.loader.local_categories()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_categories, categorie.dataframe], ignore_index=True)

    data.saver.local_categorie(df_result)
    return True

def saver_local_account(account):
    try:
        df_account = data.loader.local_accounts()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_account, account.dataframe], ignore_index=True)

    data.saver.local_account(df_result)
    return True

def saver_local_credit_card(credit_card):
    try:
        df_credit_card = data.loader.local_credit_cards()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_credit_card, credit_card.dataframe], ignore_index=True)

    data.saver.local_credit_card(df_result)
    return True
