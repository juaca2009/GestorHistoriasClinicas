from db_config import db
from dominios.solicitudes import solicitudes
from dominios.clinicas import clinicas
from dominios.administrador_general import administrador_general

class ciudad(db.Model):
    codigo_postal = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)
    solicitud = db.relationship('solicitudes', backref='solicitudes.id')
    clinica = db.relationship('clinicas', backref='clini', lazy=True)
    admin_general = db.relationship('administrador_general', backref='admin_g', lazy=True)