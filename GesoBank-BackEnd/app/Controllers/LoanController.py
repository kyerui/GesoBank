from flask import jsonify, make_response
from ..Services.LoanServices import LoanServices

class LoanController:

    @staticmethod
    def loan(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))
            value = str(data.get('value'))

            if (LoanServices.loan(userHash, passwordHash, value, db)):
                return make_response(jsonify({"message": "Loan successfully"}), 200)
            return make_response(jsonify({"message": "Loan Error"}), 400)
        except:
            return make_response(jsonify({"message": "Loan Error"}), 400)