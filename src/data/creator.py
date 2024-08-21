from pathlib import Path
import sqlite3


ROOT_DIR = Path(__file__).parent.parent
DATABASE = ROOT_DIR / "data" / "database.db"


def create_table(query: str):
    # Conecte-se ao banco de dados (ou crie um novo se não existir)
    conn = sqlite3.connect(DATABASE)

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Crie uma tabela
    cursor.execute(query)

    # Confirmar alterações
    conn.commit()

    # Feche a conexão
    cursor.close()
    conn.close()
    
    
if __name__ == "__main__":
    query = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY, 
        data DATETIME, 
        nome TEXT, 
        tipo TEXT
    )
    """
    create_table(query)