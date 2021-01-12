from db_config import db
from dominios.medicos import medicos
from dominios.administrador_clinica import administrador_clinica
from dominios.historias_clinicas import historias_clinicas

class clinicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(50), nullable=True)
    cod_postal =  db.Column(db.Integer, db.ForeignKey('ciudad.codigo_postal'), nullable=False)
    medico = db.relationship('medicos', backref='medi', lazy=True)
    admin_clinica = db.relationship('administrador_clinica', backref='admin_c', lazy=True)
    historia_c = db.relationship('historias_clinicas', backref='historia_c', lazy=True)
