import requests
import rsa
from Cryptography import rsa_func
from Enviroment import Enviroment

def register_card():
    public_key = rsa.PublicKey.load_pkcs1(Enviroment.get_env("PK").encode())

    url = 'http://localhost:5000/user/check'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": Enviroment.get_env("userHash"), "passwordHash": Enviroment.get_env("passwordHash")}
    response = requests.post(url, json=dados)

    if response.status_code == 200:

        card_name = input("Card Name: ")
        number = input("Card Number: ")
        card_number = rsa_func.rsa_encrypt_message(public_key, str(number))
        cvc = input("Card CVC: ")
        card_cvc = rsa_func.rsa_encrypt_message(public_key, str(cvc))
        year = input("Year: ")
        card_year = rsa_func.rsa_encrypt_message(public_key, str(year))
        month = input("Month: ")
        card_month = rsa_func.rsa_encrypt_message(public_key, str(month))
        card_nameUser = input("Name: ")

        url = 'http://localhost:5000/card/register' # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {
            "cardName": card_name,
            "number": card_number.hex(),
            "cvc": card_cvc.hex(),
            "year": card_year.hex(),
            "month": card_month.hex(),
            "name": card_nameUser,
            "userHash": Enviroment.get_env("userHash")
        }
        response = requests.post(url, json=dados)

        if response.status_code == 200:
            print('\nCard registered successfully')
        else:
            print('\nError registering card')
    else:
        print('\nUser not logged in')

def get_card():
    public_key = rsa.PublicKey.load_pkcs1(Enviroment.get_env("PK").encode())

    url = 'http://localhost:5000/user/check'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": Enviroment.get_env("userHash"), "passwordHash": Enviroment.get_env("passwordHash")}
    response = requests.post(url, json=dados)

    if response.status_code == 200:
        number = input("Card Number: ")
        card_number = rsa_func.rsa_encrypt_message(public_key, str(number))

        # Enviar dados do cartÃ£o para o servidor
        url = 'http://localhost:5000/card/get'
        dados = {
            "userHash": Enviroment.get_env("userHash"),
            "cardNumber": card_number.hex()
        }
        response = requests.post(url, json=dados)

        if response.status_code == 200:
            json = response.json()
            print(f"Card Name = {json['cardName']}")
            print(f"Card Number = {json['number']}")
            print(f"CVC = {json['cvc']}")
            print(f"Validity = {json['validity']}")
            print(f"Name = {json['name']}")
        else:
            print('\nError when getting card')
    else:
        print('\nUser not logged in')

def delete_card():
    public_key = rsa.PublicKey.load_pkcs1(Enviroment.get_env("PK").encode())

    url = 'http://localhost:5000/user/check'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": Enviroment.get_env("userHash"), "passwordHash": Enviroment.get_env("passwordHash")}
    response = requests.post(url, json=dados)

    if response.status_code == 200:

        number = input("Card Number: ")
        card_number = rsa_func.rsa_encrypt_message(public_key, str(number))

        url = 'http://localhost:5000/card/delete' # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {
            "passwordHash": Enviroment.get_env("passwordHash"),
            "userHash": Enviroment.get_env("userHash"),
            "cardNumber": card_number.hex()
        }
        response = requests.post(url, json=dados)

        if response.status_code == 200:
            print('\nCard deleted successfully')
        else:
            print('\nError when deleting card')
    else:
        print('\nUser not logged in')