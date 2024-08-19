from templates import account, categorie, credit_card, transaction
from pathlib import Path
import pandas as pd
import datetime
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

ROOT_DIR = Path(__file__).parent.parent


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
            "data": self._data,
            "nome": self.nome,
            "tipo": self.tipo,
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
            "data": self._data,
            "nome": self.nome,
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
            "data": self._data,
            "nome": self.nome,
            "fechamento": self.fechamento,
            "vencimento": self.vencimento,
            "limite": self.limite,
        }]
        return pd.DataFrame(data)
    
    @classmethod
    def add_credit_card(cls):
        credit_card.add_credit_card()


# Caminhos de arquivos
def check_empty_df(*args) -> bool:
    """Retorna VERDADEIRO se algum df estiver vazio"""
    df_empty = False

    # Loop
    for df in args:
        if df is None or df.empty:
            df_empty = True

    return df_empty

