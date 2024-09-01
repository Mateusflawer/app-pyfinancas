import locale

locale.setlocale(locale.LC_ALL, "")

# CRIADOR
from .creator import (
    create_transactions_table, 
    create_categories_table, 
    create_accounts_table, 
    create_credit_cards_table, 
    create_users_table,
)

# DELETADOR
from .delete import (
    delete_rows_transactions_by_id,
    delete_rows_categories_by_id,
    delete_rows_accounts_by_id,
    delete_rows_credit_cards_by_id
)

# INSERIDOR
from .insert import (
    insert_transactions_rows,
    insert_categories_rows,
    insert_accounts_rows,
    insert_credit_cards_rows,
    insert_user_registration,
)
from .loader import (
    load_transactions_by_year_and_selected_months,
    load_months_transactions_by_year,
    load_years_transactions,
    load_categories,
    load_accounts,
    load_credit_cards,
    load_users_credentials,
    load_nome_categories_by_tipo,
    load_nome_accounts,
    load_nome_credit_cards,
    load_nome_by_tipo,
)

# CONFIGURAÇÕES
from .config import (
    TRANSACTIONS,
    CATEGORIES, 
    ACCOUNTS,
    CREDIT_CARDS,
    USERS,
    TIPOS,
    ENTRADA,
    DESPESA,
)

# SELEÇÃO

__all__ = [
    # CREATE
    "create_transactions_table", 
    "create_categories_table", 
    "create_accounts_table", 
    "create_credit_cards_table", 
    "create_users_table",
    # DELETE
    "delete_rows_transactions_by_id",
    "delete_rows_categories_by_id",
    "delete_rows_accounts_by_id",
    "delete_rows_credit_cards_by_id",
    # INSERT
    "insert_transactions_rows",
    "insert_categories_rows",
    "insert_accounts_rows",
    "insert_credit_cards_rows",
    "insert_user_registration",
    # LOADER
    "load_transactions_by_year_and_selected_months",
    "load_months_transactions_by_year",
    "load_years_transactions",
    "load_categories",
    "load_accounts",
    "load_credit_cards",
    "load_users_credentials",
    "load_nome_categories_by_tipo",
    "load_nome_accounts",
    "load_nome_credit_cards",
    "load_nome_by_tipo",
    # CONFIG
    "TRANSACTIONS",
    "CATEGORIES", 
    "ACCOUNTS",
    "CREDIT_CARDS",
    "USERS",
    "TIPOS",
    "ENTRADA",
    "DESPESA",
]