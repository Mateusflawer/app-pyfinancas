import datetime
import pandas as pd

class Transaction:
    def __init__(self):
        self._data = None
        self.descricao = None
        self.categoria = None
        self.tipo = None
        self.conta = None
        self.cartao = None
        self.valor = None
        self._efetivada = None

    @property
    def data(self):
        data_hora = datetime.datetime.strptime(self._data, "%Y-%m-%d")
        return data_hora

    @data.setter
    def data(self, data):
        self._data = data
        
    @property
    def efetivada(self):
        return self._efetivada
    
    @efetivada.setter
    def efetivada(self, efetivada: bool):
        self._efetivada = "S" if efetivada else "N"

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
            "efetivada": self.efetivada,
        }]
        return pd.DataFrame(data)


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