from flask import jsonify, make_response
import datetime
from ..Services.CardServices import CardServices

class CardController:

    @staticmethod
    def register_card(data, db):
        try:
            cardName = str(data.get('cardName'))
            number = str(data.get('number'))
            cvc = str(data.get('cvc'))
            year = str(data.get('year'))
            month = str(data.get('month'))
            name = str(data.get('name'))
            userHash = str(data.get('userHash'))
            if (CardServices.register_card(cardName, number, cvc, year, month, name, userHash, db)):
                return make_response(jsonify({"message": "Card registered successfully"}), 200)
            return make_response(jsonify({"message": "Card parameters not right to put in database"}), 400)
        except:
            return make_response(jsonify({"message": "Card parameters not correct"}), 400)
    
    @staticmethod
    def get_one_card(data, db):
        try:
            userHash = str(data.get('userHash'))
            cardNumber = str(data.get('cardNumber'))

            data = CardServices.get_one_card(userHash, cardNumber, db)
            return make_response(jsonify({'cardName' : data.cardName, 'number' : data.number, 'cvc' : data.cvc, 'validity' : data.validity, 'name' : data.name}), 200)
        except:
            return make_response(400)
    
    @staticmethod
    def delete_card(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))
            cardNumber = str(data.get('cardNumber'))

            if (CardServices.delete_card(userHash, passwordHash, cardNumber, db)):
                return make_response(jsonify({"message": "Card deleted successfully"}), 200)
            return make_response(jsonify({"message": "Erro Delete"}), 400)
        except:
            return make_response(jsonify({"message": "Erro Delete"}), 400)
