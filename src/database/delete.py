from pathlib import Path
import pandas as pd
import sqlite3


ROOT_DIR = Path(__file__).parent.parent
DATABASE = ROOT_DIR / "database" / "database.db"


def delete_rows_by_id(table: str, ids: list):
    """
    Deleta linhas de uma tabela com base nos IDs fornecidos.

    :param table: Nome da tabela onde as linhas serão deletadas.
    :param ids: Lista de IDs das linhas a serem deletadas.
    :param database: Caminho para o arquivo do banco de dados SQLite.
    """
    # Conecte-se ao banco de dados
    conn = sqlite3.connect(DATABASE)

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Prepare a consulta SQL para deletar linhas com base no id
    sql = f"DELETE FROM {table} WHERE id = ?"

    # Deleta cada linha correspondente a um id na lista de ids
    for id in ids:
        cursor.execute(sql, (id,))

    # Confirmar alterações
    conn.commit()

    # Feche a conexão
    cursor.close()
    conn.close()
    

if __name__ == "__main__":
    delete_rows_by_id("transactions", [11, 12])
    