from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists
from ..Models.User import User
from ..Cryptography.AES import encrypt_message, decrypt_message
from ..Cryptography.RSA import rsa_decrypt_message, load_pem

class LoanServices:

    @staticmethod
    def loan(userHash:str, passwordHash:str, value:str, db: SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash, User.passwordHash == passwordHash)).scalar():

            user_ = db.session.query(User).filter_by(userHash=userHash).first()
            value = abs(float(rsa_decrypt_message(load_pem(decrypt_message(user_.privatekey)), bytes.fromhex(value))))

            user_.balance = decrypt_message(user_.balance)
                
            if(user_.balance == "0.00"): 
                user_.balance = str(value)
                user_.balance = encrypt_message(user_.balance)
                db.session().commit()
                db.session().close()
                return True
                
            user_.balance = str(float(user_.balance) + value)
            user_.balance = encrypt_message(user_.balance)
            db.session().commit()
            db.session().close()
            return True
        return False