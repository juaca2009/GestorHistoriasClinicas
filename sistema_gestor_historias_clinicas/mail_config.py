from app import app
from flask_mail import Mail

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'hermesclinics2020@gmail.com'
app.config['MAIL_PASSWORD'] = 'JuanCamilo99@'
mail = Mail(app)