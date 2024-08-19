import pandas as pd
from data import creator
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

# CSS
LOCAL_CSS = ROOT_DIR / "assets" / "css" / "styles.css"

# Função para ler o arquivo CSS
def local_css():
    with open(LOCAL_CSS) as f:
        return f'<style>{f.read()}</style>'

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
