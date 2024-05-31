# CSV's
LOCAL_TRANSACTIONS = "app-pyfinancas\\data\\transactions.csv"
LOCAL_CATEGORIES = "app-pyfinancas\\data\\categories.csv"
LOCAL_ACCOUNTS = "app-pyfinancas\\data\\accounts.csv"
LOCAL_CREDIT_CARDS = "app-pyfinancas\\data\\credit_cards.csv"

def local_transaction(df_transaction):
    df_transaction.to_csv(LOCAL_TRANSACTIONS, sep=";", index=False)

def local_categorie(df_transaction):
    df_transaction.to_csv(LOCAL_CATEGORIES, sep=";", index=False)

def local_account(df_transaction):
    df_transaction.to_csv(LOCAL_ACCOUNTS, sep=";", index=False)

def local_credit_card(df_transaction):
    df_transaction.to_csv(LOCAL_CREDIT_CARDS, sep=";", index=False)
