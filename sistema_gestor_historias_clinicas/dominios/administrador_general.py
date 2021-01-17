from db_config import db
from flask_login import UserMixin

class administrador_general(db.Model, UserMixin):
    nro_documento = db.Column(db.Integer, primary_key=True)
    tipo_d = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'), nullable=False)
    nombre = db.Column(db.String(40), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    cod_postal =  db.Column(db.Integer, db.ForeignKey('ciudad.codigo_postal'), nullable=False)
    contrasena = db.Column(db.String(10), nullable=False)

    def get_id(self):
        return self.nro_documento