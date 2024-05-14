import hashlib

def hash_usersenha(nome, senha):
    h = hashlib.new('sha256')
    h.update(nome.encode('utf-8'))
    h.update(senha.encode('utf-8'))
    hash_final = h.hexdigest()
    return hash_final

def hash_sla(var):
    h = hashlib.new('sha256')
    h.update(var.encode('utf-8'))
    hash_var = h.hexdigest()
    return hash_var