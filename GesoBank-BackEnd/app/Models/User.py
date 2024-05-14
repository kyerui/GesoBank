from app import db

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    userHash = db.Column(db.String, nullable=False, unique=True)
    passwordHash = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String, nullable=True, unique=True)
    balance = db.Column(db.String)
    publickey = db.Column(db.Text)
    privatekey = db.Column(db.Text)