from db_config import db

class solicitudes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)
    direccion = db.Column(db.String(30), nullable=True)
    cod_postal =  db.Column(db.Integer, db.ForeignKey('ciudad.codigo_postal'), nullable=False)
    correo = db.Column(db.String(50), nullable=False)