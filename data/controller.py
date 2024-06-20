import streamlit as st
import pandas as pd
import datetime
import locale
import data
import os

locale.setlocale(locale.LC_ALL, "portuguese_brazil")
TIPOS =  ("Entradas", "Despesas")

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
        with st.container(height=400):
            with st.spinner("Carregando dados..."):
                df_categories = data.data.loader.local_categories()
                df_accounts = data.data.loader.local_accounts()
                df_credit_cards = data.data.loader.local_credit_cards()

            transaction = data.controller.Transaction()

            transaction.descricao = st.text_area("Descrição")

            transaction.tipo = st.selectbox("Tipo", TIPOS)
            
            if transaction.tipo == "Entradas":
                categorias = df_categories[df_categories["Tipo"]=="Entradas"]["Nome"].unique()
            else:
                categorias = df_categories[df_categories["Tipo"]=="Despesas"]["Nome"].unique()

            transaction.categoria = st.selectbox("Categoria", categorias)
            credito = st.toggle("Crédito?")
            if credito:
                transaction.credit_card = st.selectbox("Cartão de crédito", df_credit_cards["Nome"].unique())
            else:
                transaction.conta = st.selectbox("Conta", df_accounts["Nome"].unique())

            transaction.data = st.date_input("Data", format="DD/MM/YYYY")
            transaction.valor = st.number_input("Valor")

        if st.button("Salvar"):
            data.controller.saver_local_transaction(transaction)
            st.rerun()

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
        categorie = data.controller.Categorie()
        categorie.nome = st.text_input("Nome")
        categorie.tipo = st.selectbox("Tipo", TIPOS)

        categorie.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

        if st.button("Salvar"):
            data.controller.data.saver_local_categorie(categorie)
            st.rerun()
    
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
        account = data.controller.Account()
        account.nome = st.text_input("Nome")

        account.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

        if st.button("Salvar"):
            data.controller.data.saver_local_account(account)
            st.rerun()
    
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
        credit_card = data.controller.CreditCard()
        credit_card.nome = st.text_input("Nome")

        credit_card.data = st.date_input("Data", format="DD/MM/YYYY", disabled=True)

        credit_card.fechamento = st.number_input("Fechamento", step=0, min_value=1, max_value=31)
        credit_card.vencimento = st.number_input("Vencimento", step=0, min_value=1, max_value=31)
        credit_card.limite = st.number_input("Limite", step=10)

        if st.button("Salvar"):
            data.controller.data.saver_local_credit_card(credit_card)
            st.rerun()

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
