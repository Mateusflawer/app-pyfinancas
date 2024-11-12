import argparse

# Cria o parser para receber argumentos da linha de comando
parser = argparse.ArgumentParser(description="Script que processa um número.")

# Adiciona um argumento chamado "numero" que será obrigatório
parser.add_argument("numero", type=int,
                    help="Um número inteiro para ser processado")

# Faz o parsing dos argumentos fornecidos
args = parser.parse_args()

# Acessa o valor do argumento 'numero'
numero = args.numero

# Exemplo de operação com o argumento
print(f"O número fornecido foi: {numero}")
print(f"O dobro do número é: {numero * 2}")
