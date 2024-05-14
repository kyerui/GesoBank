import os

def save_env(chave, valor):
    os.environ[chave] = valor
    
def get_env(chave):
    return os.environ.get(chave)