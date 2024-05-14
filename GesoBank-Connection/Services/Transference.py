import requests
import rsa
from Enviroment import Enviroment
from Cryptography import rsa_func

def transference():
    public_key = rsa.PublicKey.load_pkcs1(Enviroment.get_env("PK").encode())
    
    url = 'http://localhost:5000/user/check'  # Substitua localhost:5000 pela URL correta do seu back-end
    dados = {"userHash": Enviroment.get_env("userHash"), "passwordHash": Enviroment.get_env("passwordHash")}
    response = requests.post(url, json=dados)
    
    if response.status_code == 200:
        receiverName = input("Receiver Name: ")
        receiverCpf = input("Receiver Cpf: ")
        receiverPhone = input("Receiver Phone: ")
        value = float(input("Value: "))
        
        receiverName_rsa = rsa_func.rsa_encrypt_message(public_key, str(receiverName))
        receiverCpf_rsa = rsa_func.rsa_encrypt_message(public_key, str(receiverCpf))
        receiverPhone_rsa = rsa_func.rsa_encrypt_message(public_key, str(receiverPhone))
        value_rsa = rsa_func.rsa_encrypt_message(public_key, str("{:.2f}".format(value)))

        url = 'http://localhost:5000/transference' # Substitua localhost:5000 pela URL correta do seu back-end
        dados = {
            "userHash": Enviroment.get_env("userHash"),
            "passwordHash": Enviroment.get_env("passwordHash"),
            "value" : value_rsa.hex(),
            "receiverName": receiverName_rsa.hex(),
            "receiverCpf": receiverCpf_rsa.hex(),
            "receiverPhone": receiverPhone_rsa.hex()
        }
        response = requests.post(url, json=dados)

        if response.status_code == 200:
            print("\nTransfer completed successfully")
        else:
            print('\nError completing transfer')
    else:
        print('\nUser not logged in')