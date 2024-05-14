import requests
import rsa
from Enviroment import Enviroment
from Cryptography import rsa_func

def loan():
    public_key = rsa.PublicKey.load_pkcs1(Enviroment.get_env("PK").encode())
    
    url = 'http://localhost:5000/user/check'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": Enviroment.get_env("userHash"), "passwordHash": Enviroment.get_env("passwordHash")}
    response = requests.post(url, json=dados)
    
    if response.status_code == 200:
        value = float(input("Value: "))
        
        value_rsa = rsa_func.rsa_encrypt_message(public_key, str("{:.2f}".format(value)))

        url = 'http://localhost:5000/loan' # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {
            "userHash": Enviroment.get_env("userHash"),
            "passwordHash": Enviroment.get_env("passwordHash"),
            "value" : value_rsa.hex()
        }
        response = requests.post(url, json=dados)

        if response.status_code == 200:
            print("\nLoan completed successfully")
        else:
            print('\nError completing loan')
    else:
        print('\nUser not logged in')