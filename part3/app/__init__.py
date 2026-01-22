from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from app.api.v1 import api_v1_bp

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'super_secret_key'
    app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']

    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(api_v1_bp)

    return app
