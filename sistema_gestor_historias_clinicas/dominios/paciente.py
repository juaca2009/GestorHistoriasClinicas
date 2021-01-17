from db_config import db
from flask_login import UserMixin

class paciente(db.Model, UserMixin):
    nro_documento = db.Column(db.Integer, primary_key=True)
    tipo_d = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'), nullable=False)
    nombre = db.Column(db.String(40), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    id_historias = db.Column(db.Integer, db.ForeignKey('historias_clinicas.id'), nullable=False)
    contrasena = db.Column(db.String(10), nullable=False)