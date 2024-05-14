import rsa

# Generate RSA key pair
def new_key(nbits:int = 1024):
    public_key, private_key = rsa.newkeys(nbits)
    return public_key, private_key

def save_pem(key, type:str = "PRIVATE_KEY"):
    if (type == "PRIVATE_KEY"):
        return rsa.PrivateKey.save_pkcs1(key).decode()
    elif (type == "PUBLIC_KEY"):
        return rsa.PublicKey.save_pkcs1(key).decode()
    return "ERRO SAVE_PEM"

def load_pem(key, type:str = "PRIVATE_KEY"):
    if (type == "PRIVATE_KEY"):
        return rsa.PrivateKey.load_pkcs1(key)
    elif (type == "PUBLIC_KEY"):
        return rsa.PublicKey.load_pkcs1(key)
    return "ERRO LOAD_PEM"

# Encrypt message using RSA public key
def rsa_encrypt_message(public_key, message):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

# Decrypt message using RSA private key
def rsa_decrypt_message(private_key, encrypted_message):
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    return decrypted_message.decode()