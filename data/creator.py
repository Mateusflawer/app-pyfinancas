import pandas as pd

# CSV's
LOCAL_TRANSACTIONS = "app-pyfinancas\\data\\transactions.csv"
LOCAL_CATEGORIES = "app-pyfinancas\\data\\categories.csv"
LOCAL_ACCOUNTS = "app-pyfinancas\\data\\accounts.csv"
LOCAL_CREDIT_CARDS = "app-pyfinancas\\data\\credit_cards.csv"

TRANSACTION_TEMPLATE = {
    "Data": [],
    "Categoria": [],
    "Tipo": [],
    "Conta": [],
    "Cartão de Crédito": [],
    "Valor": [],
}

CATEGORIES_TEMPLATE = {
    "Data": [],
    "Nome": [],
    "Tipo": [],
}

ACCOUNTS_TEMPLATE = {
    "Data": [],
    "Nome": [],
}

CREDIT_CARDS_TEMPLATE = {
    "Data": [],
    "Nome": [],
    "Fechamento": [],
    "Vencimento": [],
    "Limite": [],
}

def create_local_transactions():
    df = pd.DataFrame(TRANSACTION_TEMPLATE)
    df.to_csv(LOCAL_TRANSACTIONS, sep=";",index=False)

def create_local_categories():
    df = pd.DataFrame(CATEGORIES_TEMPLATE)
    df.to_csv(LOCAL_CATEGORIES, sep=";", index=False)

def create_local_accounts():
    df = pd.DataFrame(ACCOUNTS_TEMPLATE)
    df.to_csv(LOCAL_ACCOUNTS, sep=";", index=False)

def create_local_credit_cards():
    df = pd.DataFrame(CREDIT_CARDS_TEMPLATE)
    df.to_csv(LOCAL_CREDIT_CARDS, sep=";", index=False)
