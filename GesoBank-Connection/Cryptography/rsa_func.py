import rsa
def rsa_encrypt_message(public_key, message):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message
