from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class aceptar_solicitudDto(FlaskForm):
    idS = StringField('idS')
    nombre = StringField('nombreS')
    direccion = StringField('direccionS')
    ciudad = StringField('ciudadS')
    correo = StringField('correoS')
    submit = SubmitField('Aceptar Solicitud')
