from pathlib import Path

# Caminhos de arquivos
ROOT_DIR = Path(__file__).parent.parent.parent
DATABASE = ROOT_DIR / "database" / "database.db"

ENTRADA = "Entrada"
DESPESA = "Despesa"

TIPOS = (ENTRADA, DESPESA)

TRANSACTIONS = "transactions"
ACCOUNTS = "accounts"
CATEGORIES = "categories"
CREDIT_CARDS = "credit_cards"
USERS = "users"
