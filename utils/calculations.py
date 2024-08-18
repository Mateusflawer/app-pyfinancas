import locale
from data import controller

locale.setlocale(locale.LC_ALL, "pt-br")

def dashboard_metrics(df):
    """
    Retorna: saldo, entradas e despesas calculadas com base no df recebido
    """
    entradas = df.loc[df["Tipo"]==controller.TIPOS[0], "Valor"].sum()
    despesas = df.loc[df["Tipo"]==controller.TIPOS[1], "Valor"].sum()
    saldo = entradas - despesas

    entradas = locale.currency(entradas, grouping=True)
    despesas = locale.currency(despesas, grouping=True)
    saldo = locale.currency(saldo, grouping=True)

    return saldo, entradas, despesas