import os

# Função para salvar variáveis de ambiente em um arquivo
def save(nome_arquivo, chaves:list):
    with open(nome_arquivo, 'w') as arquivo:
        for chave in chaves:
            arquivo.write(f"{chave}={os.environ.get(chave)}\n")

# Função para carregar variáveis de ambiente de um arquivo
def load(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split('=')
                os.environ[chave] = valor
    except:
        return