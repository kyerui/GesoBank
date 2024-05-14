from flask import jsonify, make_response
from ..Services.UserServices import UserServices

class UserController:

    @staticmethod
    def login_user(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))

            public_key = UserServices.login_user(userHash, passwordHash, db)
            if(public_key != None):
                return make_response(jsonify({'PK' : str(public_key)}), 200)
            return make_response('Error', 400)
        except:
            return make_response('Error', 400)

    @staticmethod
    def register_user(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))
            name = str(data.get('name'))
            cpf = str(data.get('cpf'))
            phone = str(data.get('phone'))

            if(UserServices.register_user(userHash, passwordHash, name, cpf, phone, db)):
                return make_response(jsonify({"message": "User registered successfully"}), 200)
            return make_response('Error', 400)
        except:
            return make_response('Error', 400)
    
    @staticmethod
    def get_user_data(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))

            data = UserServices.get_user_data(userHash, passwordHash, db)

            return make_response(jsonify({'name': data.name, 'balance': data.balance, 'cpf': data.cpf, 'phone': data.phone}), 200)
        except:
            return make_response('Error', 400)
        
    @staticmethod
    def get_user_balance(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))

            data = UserServices.get_user_data(userHash, passwordHash, db)

            return make_response(jsonify({'balance' : data.balance}), 200)
        except:
            return make_response('Error', 400)
        
    @staticmethod
    def check_user(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))

            if (UserServices.check_user(userHash, passwordHash, db)):
                return make_response(jsonify({"message": "User logged successfully"}), 200)
            return make_response('Error', 400)
        except:
            return make_response('Error', 400)