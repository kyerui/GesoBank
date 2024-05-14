from Cryptography import hash
import requests
from Enviroment.Enviroment import save_env

def register_user():
    user = input("Username: ")
    password = input("Password: ")
    name = input("Name: ")
    cpf = input("CPF: ")  
    phone = input("Phone: ")
    
    userHash = hash.hash_sla(user)
    passwordHash = hash.hash_sla(password)
    
    url = 'http://localhost:5000/user/register'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": userHash, "passwordHash": passwordHash, "name": name, "cpf": cpf, "phone": phone}
    response = requests.post(url, json=dados)
    if response.status_code == 200:
        print("\nSuccessfully Register")  # Exibindo a resposta do back-end
    else:
        print('\nUnable to register user')

def login():
    user = input("Username: ")
    password = input("Password: ")
    
    userHash = hash.hash_sla(user)
    passwordHash = hash.hash_sla(password)
    
    url = 'http://localhost:5000/user/login'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": userHash, "passwordHash": passwordHash}
    response = requests.post(url, json=dados)

    if response.status_code == 200:
        json = response.json()
        save_env('PK', json['PK'])
        save_env('userHash', userHash)
        save_env('passwordHash', passwordHash)
        print("\nSuccessfully Login")
        return True
    else:
        print('\nLogin Invalid')
        return False