from data import creator

# CSV's
LOCAL_TRANSACTIONS = creator.LOCAL_TRANSACTIONS
LOCAL_CATEGORIES = creator.LOCAL_CATEGORIES
LOCAL_ACCOUNTS = creator.LOCAL_ACCOUNTS
LOCAL_CREDIT_CARDS = creator.LOCAL_CREDIT_CARDS


def local_transaction(df_transaction):
    df_transaction.to_csv(LOCAL_TRANSACTIONS, sep=";", index=False)

def local_categorie(df_transaction):
    df_transaction.to_csv(LOCAL_CATEGORIES, sep=";", index=False)

def local_account(df_transaction):
    df_transaction.to_csv(LOCAL_ACCOUNTS, sep=";", index=False)

def local_credit_card(df_transaction):
    df_transaction.to_csv(LOCAL_CREDIT_CARDS, sep=";", index=False)
