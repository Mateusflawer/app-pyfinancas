import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__)

# CSV's
LOCAL_TRANSACTIONS = ROOT_DIR.parent / "transactions.csv"
LOCAL_CATEGORIES = ROOT_DIR.parent / "categories.csv"
LOCAL_ACCOUNTS = ROOT_DIR.parent / "accounts.csv"
LOCAL_CREDIT_CARDS = ROOT_DIR.parent / "credit_cards.csv"

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
