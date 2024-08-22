import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
import sqlite3

ROOT_DIR = Path(__file__).parent.parent

DATABASE = ROOT_DIR / "database" / "database.db"

def adapt_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def convert_datetime(s):
    return datetime.strptime(s.decode(), '%Y-%m-%d %H:%M:%S')


# Ler transações
def load_per_period(table: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    # Adaptadores personalizados para datetime
    sqlite3.register_adapter(datetime, adapt_datetime)
    sqlite3.register_converter("datetime", convert_datetime)
    
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    query = f"""
        SELECT * FROM {table} 
        WHERE data BETWEEN ? AND ? 
    """
    cursor.execute(query, (start_date, end_date))
    
    description = cursor.description
    columns = [descript[0] for descript in description]
    transactions = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # Converte os resultados em um DataFrame do pandas
    df = pd.DataFrame(transactions, columns=columns)
    return df


# Carrega exemplo de transações
def example_transactions():
    # Gerando dados fictícios para entradas e despesas mensais
    categorias = ['Salário', 'Freelance', 'Investimentos', 'Presentes', 'Outros']
    entradas = [4000, 1500, 800, 200, 300]
    despesas = [1000, 500, 200, 150, 100]

    # Expandindo os dados para múltiplos meses
    datas = pd.date_range(start='2023-01-01', periods=6, freq='ME')
    data_expanded = {
        'data': [],
        'categoria': [],
        'tipo': [],
        'valor': []
    }

    for data in datas:
        for i, categoria in enumerate(categorias):
            data_expanded['data'].append(data)
            data_expanded['categoria'].append(categoria)
            data_expanded['tipo'].append('Entrada')
            data_expanded['valor'].append(entradas[i])
            data_expanded['data'].append(data)
            data_expanded['categoria'].append(categoria)
            data_expanded['tipo'].append('Despesa')
            data_expanded['valor'].append(despesas[i])

    # Criação do DataFrame
    df = pd.DataFrame(data_expanded)
    return df


if __name__ == "__main__":
    df = load_per_period("transactions", datetime.now() - timedelta(days=1), datetime.now())
    print(df)
    