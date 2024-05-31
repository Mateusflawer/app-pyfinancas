from data import loader, creator, saver
import pandas as pd
import datetime
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

class Transaction:
    def __init__(self):
        self.data = None
        self.hora = None
        self.categoria = None
        self.tipo = None
        self.conta = None
        self.credit_card = None
        self.valor = None

    @property
    def data_hora(self):
        data_hora_str = f"{self.data} {self.hora}"
        data_hora = datetime.datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M:%S")
        return data_hora

    @property
    def dataframe(self):
        data = [{
            "Data": self.data_hora,
            "Categoria": self.categoria,
            "Tipo": self.tipo,
            "Conta": self.conta,
            "Cartão de Crédito": self.credit_card,
            "Valor": self.valor,
        }]
        return pd.DataFrame(data)

class Categorie:
    def __init__(self):
        self.nome = None
        self.data = None
        self.hora = None
        self.tipo = None

    @property
    def data_hora(self):
        data_hora_str = f"{self.data} {self.hora}"
        data_hora = datetime.datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M:%S")
        return data_hora

    @property
    def dataframe(self):
        data = [{
            "Data": self.data_hora,
            "Nome": self.nome,
            "Tipo": self.tipo,
        }]
        return pd.DataFrame(data)
    
class Account:
    def __init__(self):
        self.nome = None
        self.data = None
        self.hora = None

    @property
    def data_hora(self):
        data_hora_str = f"{self.data} {self.hora}"
        data_hora = datetime.datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M:%S")
        return data_hora

    @property
    def dataframe(self):
        data = [{
            "Data": self.data_hora,
            "Nome": self.nome,
        }]
        return pd.DataFrame(data)
    
class CreditCard:
    def __init__(self):
        self.nome = None
        self.data = None
        self.hora = None
        self.fechamento = None
        self.vencimento = None
        self.limite = None

    @property
    def data_hora(self):
        data_hora_str = f"{self.data} {self.hora}"
        data_hora = datetime.datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M:%S")
        return data_hora

    @property
    def dataframe(self):
        data = [{
            "Data": self.data_hora,
            "Nome": self.nome,
            "Fechamento": self.fechamento,
            "Vencimento": self.vencimento,
            "Limite": self.limite,
        }]
        return pd.DataFrame(data)
    

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

def loader_transactions():
    try:
        loader.local_transactions()
    except FileNotFoundError:
        creator.create_local_transactions()

def loader_categories():
    try:
        loader.local_categories()
    except FileNotFoundError:
        creator.create_local_categories()

def loader_accounts():
    try:
        loader.local_accounts()
    except FileNotFoundError:
        creator.create_local_accounts()

def loader_credit_cards():
    try:
        loader.local_credit_cards()
    except FileNotFoundError:
        creator.create_local_credit_cards()

def saver_local_transaction(transaction):
    try:
        df_transaction = loader.local_transactions()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_transaction, transaction.dataframe], ignore_index=True)

    saver.local_transaction(df_result)
    return True

def saver_local_categorie(categorie):
    try:
        df_categories = loader.local_categories()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_categories, categorie.dataframe], ignore_index=True)

    saver.local_categorie(df_result)
    return True

def saver_local_account(account):
    try:
        df_account = loader.local_accounts()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_account, account.dataframe], ignore_index=True)

    saver.local_account(df_result)
    return True

def saver_local_credit_card(credit_card):
    try:
        df_credit_card = loader.local_credit_cards()
    except FileNotFoundError:
        return False
    
    df_result = pd.concat([df_credit_card, credit_card.dataframe], ignore_index=True)

    saver.local_credit_card(df_result)
    return True