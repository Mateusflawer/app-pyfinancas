from pathlib import Path

# Caminhos de arquivos
ROOT_DIR = Path(__file__).parent.parent.parent
DATABASE = ROOT_DIR / "database" / "database.db"

ENTRADA = "Entrada"
SAIDA = "Saida"

TIPOS = (ENTRADA, SAIDA)

TRANSACTIONS = "transactions"
ACCOUNTS = "accounts"
CATEGORIES = "categories"
USERS = "users"
