import locale

locale.setlocale(locale.LC_ALL, "pt-br")

def dashboard_metrics(df):
    """
    Retorna: saldo, entradas e despesas calculadas com base no df recebido
    """
    entradas = df.loc[df["Tipo"]=="Entradas", "Valor"].sum()
    despesas = df.loc[df["Tipo"]=="Despesas", "Valor"].sum()
    saldo = entradas - despesas

    entradas = locale.currency(entradas, grouping=True)
    despesas = locale.currency(despesas, grouping=True)
    saldo = locale.currency(saldo, grouping=True)

    return saldo, entradas, despesas