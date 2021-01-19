from db_config import db
from dominios.administrador_general import administrador_general
from dominios.administrador_clinica import administrador_clinica
from dominios.medicos import medicos
from dominios.paciente import paciente

class tipo_documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    admin_general = db.relationship('administrador_general', backref='adming', lazy=True)
    medico = db.relationship('medicos', backref='med', lazy=True)
    admin_clinica = db.relationship('administrador_clinica', backref='adminc', lazy=True)
    pacient = db.relationship('paciente', backref='pac', lazy=True)