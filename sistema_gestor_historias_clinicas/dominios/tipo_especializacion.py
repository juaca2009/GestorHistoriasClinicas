from db_config import db
from dominios.medicos import medicos

class tipo_especializacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    medico = db.relationship('medicos', backref='medi', lazy=True)