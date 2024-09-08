import datetime
import pandas as pd
import streamlit as st

class Transaction:
    def __init__(self):
        self._lancamento = None
        self.descricao = None
        self.categoria = None
        self.tipo = None
        self.conta = None
        self.valor = None
        self._efetivada = None

    @property
    def lancamento(self):
        data_hora = datetime.datetime.strptime(self._lancamento, "%Y-%m-%d")
        return data_hora

    @lancamento.setter
    def lancamento(self, data):
        self._lancamento = data
        
    @property
    def efetivada(self):
        return self._efetivada
    
    @efetivada.setter
    def efetivada(self, efetivada: bool):
        self._efetivada = "Sim" if efetivada else "Nao"

    @property
    def dataframe(self):
        data = [{
            "data": self._lancamento,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "tipo": self.tipo,
            "conta": self.conta,
            "valor": self.valor,
            "efetivada": self.efetivada,
            "user_id": st.session_state["user_id"]
        }]
        return pd.DataFrame(data)


class Categorie:
    def __init__(self):
        self.nome = None
        self._lancamento = None
        self.tipo = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._lancamento, "%Y-%m-%d")
        return data_hora

    @data.setter
    def data(self, data):
        self._lancamento = data

    @property
    def dataframe(self):
        data = [{
            "data": self._lancamento,
            "nome": self.nome,
            "tipo": self.tipo,
            "user_id": st.session_state["user_id"]
        }]
        return pd.DataFrame(data)
    

class Account:
    def __init__(self):
        self.nome = None
        self._lancamento = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._lancamento, "%Y-%m-%d %H:%M:%S")
        return data_hora

    @data.setter
    def data(self, data):
        self._lancamento = data

    @property
    def dataframe(self):
        data = [{
            "data": self._lancamento,
            "nome": self.nome,
            "user_id": st.session_state["user_id"]
        }]
        return pd.DataFrame(data)
    

class CreditCard:
    def __init__(self):
        self.nome = None
        self._lancamento = None
        self.fechamento = None
        self.vencimento = None
        self.limite = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._lancamento, "%Y-%m-%d")
        return data_hora

    @data.setter
    def data(self, data):
        self._lancamento = data

    @property
    def dataframe(self):
        data = [{
            "data": self._lancamento,
            "nome": self.nome,
            "fechamento": self.fechamento,
            "vencimento": self.vencimento,
            "limite": self.limite,
            "user_id": st.session_state["user_id"]
        }]
        return pd.DataFrame(data)
    