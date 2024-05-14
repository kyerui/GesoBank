from flask import Flask, request
from ..Controllers.UserController import UserController
from ..Controllers.CardController import CardController
from ..Controllers.TransferenceController import TransferenceController
from ..Controllers.LoanController import LoanController
from flask_sqlalchemy import SQLAlchemy

def registrar_rotas(app:Flask, db: SQLAlchemy):

    ###############
    ##  Usuário  ##
    ###############

    @app.route('/user/login', methods=['POST'])
    def login_user():
        data = request.get_json()
        return UserController.login_user(data, db)

    @app.route('/user/register', methods=['POST'])
    def register_user():
        data = request.get_json() 
        return UserController.register_user(data, db)

    @app.route('/user/data', methods=['POST'])
    def user_data():
        data = request.get_json()
        return UserController.get_user_data(data, db)

    @app.route('/user/balance', methods=['POST'])
    def user_balance():
        data = request.get_json()
        return UserController.get_user_balance(data, db)

    @app.route('/user/check', methods=['POST'])
    def check_user():
        data = request.get_json() 
        return UserController.check_user(data, db)
    
    #####################
    ##  Transferencia  ##
    #####################

    @app.route('/transference', methods=['POST'])
    def transference():
        data = request.get_json()
        return TransferenceController.transference(data, db)
    
    ##################
    ##  Empréstimo  ##
    ##################

    @app.route('/loan', methods=['POST'])
    def loan():
        data = request.get_json()
        return LoanController.loan(data, db)

    ##############
    ##  Cartão  ##
    ##############

    @app.route('/card/register', methods=['POST'])
    def register_card():
        data = request.get_json() 
        return CardController.register_card(data, db)
    
    @app.route('/card/get', methods=['POST'])
    def get_one_card():
        data = request.get_json() 
        return CardController.get_one_card(data, db)
    
    @app.route('/card/delete', methods=['POST'])
    def delete_card():
        data = request.get_json() 
        return CardController.delete_card(data, db)