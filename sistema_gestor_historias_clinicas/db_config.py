from app import app
from flaskext.mysql import MySQL
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '222146'
app.config['MYSQL_DATABASE_PASSWORD'] = 'juancamilo99'
app.config['MYSQL_DATABASE_DB'] = 'juancamilo99_historiasc'
app.config['MYSQL_DATABASE_HOST'] = 'mysql-juancamilo99.alwaysdata.net'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://222146:juancamilo99@mysql-juancamilo99.alwaysdata.net:3306/juancamilo99_historiasc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql.init_app(app)
db = SQLAlchemy(app)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'b56cde8c29107c55dce5f0ff90c59d12'
app.config['SECRET_KEY'] = 'b56cde8c29107c55dce5f0ff90c59d12'
app.config['JWT_ALGORITHM'] = 'HS512'
app.config['JWT_EXP_DELTA_SECONDS'] = 60
jwt = JWTManager(app)