from flask import jsonify, make_response
from ..Services.TransferenceServices import TransferenceServices

class TransferenceController:

    @staticmethod
    def transference(data, db):
        try:
            userHash = str(data.get('userHash'))
            passwordHash = str(data.get('passwordHash'))
            value = str(data.get('value'))
            receiverName = str(data.get('receiverName'))
            receiverCpf = str(data.get('receiverCpf'))
            receiverPhone = str(data.get('receiverPhone'))
            
            if (TransferenceServices.transference(userHash, passwordHash, value, receiverName, receiverCpf, receiverPhone, db)):
                return make_response(jsonify({"message": "Transference made successfully"}), 200)
            return make_response(jsonify({"message": "Transference Error"}), 400)
        except:
            return make_response(jsonify({"message": "Transference Error"}), 400)