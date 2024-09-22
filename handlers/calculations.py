import locale
from database import controller

locale.setlocale(locale.LC_ALL, "")

def dashboard_metrics(df):
    """
    Retorna: saldo, entradas e despesas calculadas com base no df recebido
    """
    entradas = df.loc[df["tipo"]==controller.ENTRADA, "valor"].sum()
    despesas = df.loc[df["tipo"]==controller.SAIDA, "valor"].sum()
    saldo = entradas - despesas

    entradas = f'R$ {entradas:,.2f}'.replace('.', ',').replace(',', '.')
    despesas = f'R$ {despesas:,.2f}'.replace('.', ',').replace(',', '.')
    saldo = f'R$ {saldo:,.2f}'.replace('.', ',').replace(',', '.')

    return entradas, despesas, saldo
