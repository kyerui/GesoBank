from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import appdirs

db = SQLAlchemy()

def create_app():
    from app.Cryptography.Environments import load

    load(os.path.join(appdirs.user_data_dir(), 'GesoBankEnvironments.env'))

    if (os.environ.get('GesoBank_Key') is None and os.environ.get('GesoBank_Iv') is None):
        from app.Cryptography.AES import generate_key_iv
        generate_key_iv()
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gesodata.db'
    db.init_app(app)
    
    from app.Routes.Routes import registrar_rotas
    
    registrar_rotas(app, db)
    
    migrate = Migrate(app, db)
    return app