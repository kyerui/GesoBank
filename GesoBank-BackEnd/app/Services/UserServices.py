from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exists
from ..Models.User import User
from ..Cryptography.RSA import new_key, save_pem
from ..Cryptography.AES import encrypt_message, decrypt_message

class UserServices:

    @staticmethod
    def login_user(userHash:str, passwordHash:str, db: SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash, User.passwordHash == passwordHash)).scalar():
            userData = db.session.query(User).filter_by(userHash=userHash, passwordHash=passwordHash).first()
            return userData.publickey
        return None

    @staticmethod
    def register_user(userHash:str, passwordHash:str, name:str, cpf:str, phone:str, db: SQLAlchemy):
        if db.session.query(exists().where(User.userHash != userHash)):

            public_key, private_key = new_key()

            encrypt_cpf = encrypt_message(cpf)
            encrypt_balance = encrypt_message("0.00")

            private_key = save_pem(private_key)
            public_key = save_pem(public_key, "PUBLIC_KEY")

            encrypt_private_key = encrypt_message(str(private_key))

            new_user = User(userHash = userHash, name = name, cpf = encrypt_cpf, phone = phone, passwordHash = passwordHash, privatekey = encrypt_private_key, publickey = str(public_key), balance = encrypt_balance)

            db.session().add(new_user)
            db.session().commit()
            db.session().close()

            return True
        return False
    
    @staticmethod
    def get_user_balance(userHash:str, passwordHash:str, db: SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash, User.passwordHash == passwordHash)).scalar():
            userData = db.session.query(User).filter_by(userHash=userHash, passwordHash=passwordHash).first()
            userData.balance = decrypt_message(userData.balance)
            return userData
        return None

    @staticmethod
    def get_user_data(userHash:str, passwordHash:str, db: SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash, User.passwordHash == passwordHash)).scalar():
            userData = db.session.query(User).filter_by(userHash=userHash, passwordHash=passwordHash).first()
            userData.balance = decrypt_message(userData.balance)
            userData.cpf = decrypt_message(userData.cpf)
            return userData
        return None
    
    @staticmethod
    def check_user(userHash:str, passwordHash:str, db: SQLAlchemy):
        if db.session.query(exists().where(User.userHash == userHash, User.passwordHash == passwordHash)).scalar():
            return True
        return False