import pandas as pd

# Função para ler o arquivo CSS
def local_css(file_name):
    with open(file_name) as f:
        return f'<style>{f.read()}</style>'
    

def get_data():
    # Gerando dados fictícios para entradas e despesas mensais
    categorias = ['Salário', 'Freelance', 'Investimentos', 'Presentes', 'Outros']
    entradas = [4000, 1500, 800, 200, 300]
    despesas = [1000, 500, 200, 150, 100]

    # Expandindo os dados para múltiplos meses
    datas = pd.date_range(start='2023-01-01', periods=6, freq='M')
    data_expanded = {
        'Data': [],
        'Categoria': [],
        'Tipo': [],
        'Valor': []
    }

    for data in datas:
        for i, categoria in enumerate(categorias):
            data_expanded['Data'].append(data)
            data_expanded['Categoria'].append(categoria)
            data_expanded['Tipo'].append('Entradas')
            data_expanded['Valor'].append(entradas[i])
            data_expanded['Data'].append(data)
            data_expanded['Categoria'].append(categoria)
            data_expanded['Tipo'].append('Despesas')
            data_expanded['Valor'].append(despesas[i])

    # Criação do DataFrame
    df = pd.DataFrame(data_expanded)
    return df