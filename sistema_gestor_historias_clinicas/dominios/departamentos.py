from db_config import db
from dominios.ciudad import ciudad

class departamentos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    ciudad = db.relationship('ciudad', backref='ciu', lazy=True)