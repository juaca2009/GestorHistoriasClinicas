from db_config import db
import datetime

class entradas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sintomas = db.Column(db.String(500), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    operaciones_recientes = db.Column(db.String(500), nullable=False)
    diagnosticos = db.Column(db.String(500), nullable=False)
    medicamentos = db.Column(db.String(500), nullable=True)
    examenes = db.Column(db.String(500), nullable=True)
    id_historias = db.Column(db.Integer, db.ForeignKey('historias_clinicas.id'), nullable=False)