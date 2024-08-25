import locale
from database import controller

locale.setlocale(locale.LC_ALL, "")

ENTRADA = controller.ENTRADA
DESPESA = controller.DESPESA

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

    return entradas, despesas, saldo
