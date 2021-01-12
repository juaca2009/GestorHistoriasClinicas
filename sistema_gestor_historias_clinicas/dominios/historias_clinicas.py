from db_config import db
from dominios.paciente import paciente
from dominios.entradas import entradas

class historias_clinicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nro_documento = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(40), nullable=False)
    apellidos = db.Column(db.String(40), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    id_clinica = db.Column(db.Integer, db.ForeignKey('clinicas.id'), nullable=False)
    entrada = db.relationship('entradas', backref='entra', lazy=True)
    pacient = db.relationship('paciente', backref='paci', lazy=True)