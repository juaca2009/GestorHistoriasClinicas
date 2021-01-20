from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class eliminar_adminPDto(FlaskForm):
    nombreAp = StringField('nombreAp')
    apellidosAp = StringField('apellidosAp')
    documentoAp = StringField('documentoAp')
    email = StringField('email')
    telefonoAp = StringField('telefonoAp')
    ciudadAp = StringField('ciudadAp')
    submit = SubmitField('Eliminar Administrador')
