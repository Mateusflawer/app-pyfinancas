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

    for _, row in df.iterrows():

        # Adicione uma linha
        cursor.execute(f"""
            INSERT INTO {table} {str(tuple(row.index))} 
            VALUES {str(tuple(row.values))}
        """)

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
    