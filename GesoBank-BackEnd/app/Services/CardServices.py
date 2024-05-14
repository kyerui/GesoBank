from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists
from ..Models.Card import Card
from ..Models.User import User
from ..Cryptography.AES import encrypt_message, decrypt_message
from ..Cryptography.RSA import rsa_decrypt_message, load_pem

class CardServices:

    @staticmethod
    def register_card(cardName:str, number:str, cvc:str, year:str, month:str, name:str, userHash:str, db: SQLAlchemy):
        if(db.session.query(exists().where(User.userHash == userHash))).scalar():
            userData = db.session.query(User).filter_by(userHash=userHash).first()

            year = rsa_decrypt_message(load_pem(decrypt_message(userData.privatekey)), bytes.fromhex(year))
            month = rsa_decrypt_message(load_pem(decrypt_message(userData.privatekey)), bytes.fromhex(month))
            validity = str(datetime.date(int(year), int(month), 1))

            number = rsa_decrypt_message(load_pem(decrypt_message(userData.privatekey)), bytes.fromhex(number))
            cvc = rsa_decrypt_message(load_pem(decrypt_message(userData.privatekey)), bytes.fromhex(cvc))
                
            encrypt_number = encrypt_message(number)
            encrypt_cvc = encrypt_message(cvc)
            encrypt_validity = encrypt_message(validity)

            new_card = Card(cardName = cardName, number = encrypt_number, cvc = encrypt_cvc, validity = encrypt_validity, name = name, userHash = userHash)
            db.session().add(new_card)
            db.session().commit()
            db.session().close()
            return True
        return False 
    
    @staticmethod
    def get_one_card(userHash:str, cardNumber:str, db:SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash)).scalar():
            userData = db.session.query(User).filter_by(userHash=userHash).first()
            cardNumber = rsa_decrypt_message(load_pem(decrypt_message(userData.privatekey)), bytes.fromhex(cardNumber))
            cardNumber = encrypt_message(cardNumber)
            
            if db.session.query(exists().where(Card.number == cardNumber)).scalar():
                p1 = db.session.query(Card).filter_by(number=cardNumber, userHash=userHash).first()
                p1.number = decrypt_message(p1.number)
                p1.cvc = decrypt_message(p1.cvc)
                validity = datetime.strptime(decrypt_message(p1.validity), '%Y-%m-%d')
                p1.validity = (f"{validity.month}-{validity.year}")
                return p1
        return None  

    @staticmethod
    def delete_card(userHash:str, passwordHash:str, cardNumber:str, db:SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash, User.passwordHash == passwordHash)).scalar():

            userData = db.session.query(User).filter_by(userHash=userHash).first()
            cardNumber = rsa_decrypt_message(load_pem(decrypt_message(userData.privatekey)), bytes.fromhex(cardNumber))
            cardNumber = encrypt_message(cardNumber)
            
            if db.session.query(exists().where(Card.number == cardNumber)).scalar():
                p1 = db.session.query(Card).filter_by(number=cardNumber, userHash=userHash).first()
                db.session().delete(p1)
                db.session().commit()
                db.session().close()
                return True
        return False