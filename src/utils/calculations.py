import locale
from data import controller

locale.setlocale(locale.LC_ALL, "pt-br")

ENTRADA = "Entrada"
DESPESA = "Despesa"

def dashboard_metrics(df):
    """
    Retorna: saldo, entradas e despesas calculadas com base no df recebido
    """
    entradas = df.loc[df["tipo"]==ENTRADA, "valor"].sum()
    despesas = df.loc[df["tipo"]==DESPESA, "valor"].sum()
    saldo = entradas - despesas

    entradas = locale.currency(entradas, grouping=True)
    despesas = locale.currency(despesas, grouping=True)
    saldo = locale.currency(saldo, grouping=True)

    return saldo, entradas, despesas