import requests
from Enviroment import Enviroment

def get_user_balance():

    url = 'http://localhost:5000/user/check'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": Enviroment.get_env("userHash"), "passwordHash": Enviroment.get_env("passwordHash")}
    response = requests.post(url, json=dados)

    if response.status_code == 200:
        url = 'http://localhost:5000/user/balance'
        dados = {
            "userHash": Enviroment.get_env("userHash"),
            "passwordHash": Enviroment.get_env("passwordHash")
        }
        response = requests.post(url, json=dados)

        if response.status_code == 200:
            json = response.json()
            print(f"\nBalance = {json['balance']}")
        else:
            print('Error catching user balance')
    else:
        print('User not logged in')

def get_user_data():

    url = 'http://localhost:5000/user/check'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": Enviroment.get_env("userHash"), "passwordHash": Enviroment.get_env("passwordHash")}
    response = requests.post(url, json=dados)

    if response.status_code == 200:
        url = 'http://localhost:5000/user/data'
        dados = {
            "userHash": Enviroment.get_env("userHash"),
            "passwordHash": Enviroment.get_env("passwordHash")
        }
        response = requests.post(url, json=dados)

        if response.status_code == 200:
            json = response.json()
            print(f"Balance = {json['balance']}")
            print(f"Name = {json['name']}")
            print(f"CPF = {json['cpf']}")
            print(f"Phone = {json['phone']}")
        else:
            print('Error catching user data')
    else:
        print('User not logged in')