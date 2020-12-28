from app import app
from flaskext.mysql import MySQL
from flask_jwt_extended import JWTManager

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '222146'
app.config['MYSQL_DATABASE_PASSWORD'] = 'juancamilo99@'
app.config['MYSQL_DATABASE_DB'] = 'juancamilo99_historiasc'
app.config['MYSQL_DATABASE_HOST'] = 'mysql-juancamilo99.alwaysdata.net'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'mySecretKey'
app.config['JWT_ALGORITHM'] = 'HS512'
app.config['JWT_EXP_DELTA_SECONDS'] = 60
jwt = JWTManager(app)