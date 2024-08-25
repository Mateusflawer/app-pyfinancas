from pathlib import Path
import pandas as pd
import sqlite3


ROOT_DIR = Path(__file__).parent.parent
DATABASE = ROOT_DIR / "database" / "database.db"


def insert_rows(table: str, df: pd.DataFrame):
    # Conecte-se ao banco de dados (ou crie um novo se não existir)
    conn = sqlite3.connect(DATABASE)

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Obtenha os nomes das colunas do DataFrame
    columns = ', '.join(df.columns)
    placeholders = ', '.join(['?'] * len(df.columns))

    # Prepare a consulta SQL
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    # Insira as linhas
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row.values))

    # Confirmar alterações
    conn.commit()

    # Feche a conexão
    cursor.close()
    conn.close()

    

if __name__ == "__main__":
    dados = {
        "data": ["2024-08-20"],
        "nome": ["teste"]
    }
    df = pd.DataFrame(dados)
    insert_rows("accounts", df)