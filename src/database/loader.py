from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import sqlite3

ROOT_DIR = Path(__file__).parent.parent

DATABASE = ROOT_DIR / "database" / "database.db"

# Ler transações
def load_per_period(table: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)
    
    query = f"""
        SELECT * FROM {table} 
        WHERE data BETWEEN ? AND ? 
    """
    
    params = (start_date, end_date)
    
    df = pd.read_sql_query(sql=query, con=conn, params=params)
    return df


def load_nome_by_tipo(table:str, tipo: str) -> pd.DataFrame:
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table}
        WHERE tipo = ? GROUP BY nome
    """
    
    params = (tipo,)
    df = pd.read_sql_query(query, conn, params=params)
    return df


def load_nome(table: str):
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table} GROUP BY nome
    """
    
    df = pd.read_sql_query(query, conn)
    return df


if __name__ == "__main__":
    df = load_per_period(
        "transactions", datetime.now() - timedelta(days=1), datetime.now()
    )
    print(df)
    