from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from ..Cryptography.Environments import save
import os
import appdirs
import random
import string

def generate_key_iv():
    characters = string.ascii_letters + string.digits
    # Gerando uma chave aleatória (32 bytes para AES-256)
    os.environ['GesoBank_Key'] = ''.join(random.choice(characters) for i in range(32))
    # Gerando um IV aleatório (16 bytes para AES)
    os.environ['GesoBank_Iv'] = ''.join(random.choice(characters) for i in range(16))
    # Salvando localmente
    save(os.path.join(appdirs.user_data_dir(), 'GesoBankEnvironments.env'), ['GesoBank_Key', 'GesoBank_Iv'])

def encrypt_message(plaintext, key=os.environ.get('GesoBank_Key'), iv=os.environ.get('GesoBank_Iv')):
    key = bytes(key, encoding="ascii")
    iv = bytes(iv, encoding="ascii")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return b64encode(ciphertext)

def decrypt_message(ciphertext, key=os.environ.get('GesoBank_Key'), iv=os.environ.get('GesoBank_Iv')):
    key = bytes(key, encoding="ascii")
    iv = bytes(iv, encoding="ascii")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(b64decode(ciphertext))
    plaintext = unpad(padded_data, AES.block_size)
    return plaintext.decode()