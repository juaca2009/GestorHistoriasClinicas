from flask import Flask
from flask_cors import CORS, cross_origin
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.login_view = 'inicio_sesion'

encriptador = Bcrypt()

CORS(app)