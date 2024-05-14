from app import db

class Card(db.Model):
    tablename = 'card'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    cardName = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False, unique=True)
    cvc = db.Column(db.String, nullable=False)
    validity = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    userHash = db.Column(db.String, nullable=False)