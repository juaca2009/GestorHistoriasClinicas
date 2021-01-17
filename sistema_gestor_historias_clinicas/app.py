from flask import Flask
from flask_cors import CORS, cross_origin
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
CORS(app)