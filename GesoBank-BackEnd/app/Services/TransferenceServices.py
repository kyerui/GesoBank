from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists
from ..Models.User import User
from ..Cryptography.AES import encrypt_message, decrypt_message
from ..Cryptography.RSA import rsa_decrypt_message, load_pem

class TransferenceServices:

    @staticmethod
    def transference(userHash:str, passwordHash:str, value:str, receiverName:str, receiverCpf:str, receiverPhone:str, db: SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash,User.passwordHash == passwordHash)):

            p1 = db.session.query(User).filter_by(userHash=userHash).first()
                
            receiverCpf = str(rsa_decrypt_message(load_pem(decrypt_message(p1.privatekey)), bytes.fromhex(receiverCpf)))
            receiverName = str(rsa_decrypt_message(load_pem(decrypt_message(p1.privatekey)), bytes.fromhex(receiverName)))
            receiverPhone = str(rsa_decrypt_message(load_pem(decrypt_message(p1.privatekey)), bytes.fromhex(receiverPhone)))
            receiverCpf = encrypt_message(receiverCpf)

            if db.session.query(exists().where(User.name == receiverName, User.cpf == receiverCpf, User.phone == receiverPhone)):
                p1.balance = decrypt_message(p1.balance)

                value = float(rsa_decrypt_message(load_pem(decrypt_message(p1.privatekey)), bytes.fromhex(value)))

                p2 = db.session.query(User).filter_by(cpf=receiverCpf).first()
                p2.balance = decrypt_message(p2.balance)

                if(float(p1.balance) >= value):
                    p1.balance = str(float(p1.balance) - value)
                    p1.balance = encrypt_message(p1.balance)
                    if(p2.balance == "0.00"): 
                        p2.balance = str(value)
                        p2.balance = encrypt_message(p2.balance)
                        db.session().commit()
                        db.session().close()
                        return True
                    p2.balance = str(float(p2.balance) + value)
                    p2.balance = encrypt_message(p2.balance)
                    db.session().commit()
                    db.session().close()
                    return True
        return False