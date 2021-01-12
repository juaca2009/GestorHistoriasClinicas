from db_config import db

class medicos(db.Model):
    nro_documento = db.Column(db.Integer, primary_key=True)
    tipo_d = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'), nullable=False)
    nombre = db.Column(db.String(40), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    id_clinica = db.Column(db.Integer, db.ForeignKey('clinicas.id'), nullable=False)
    id_espc = db.Column(db.Integer, db.ForeignKey('tipo_especializacion.id'), nullable=False)
    contrasena = db.Column(db.String(10), nullable=False)