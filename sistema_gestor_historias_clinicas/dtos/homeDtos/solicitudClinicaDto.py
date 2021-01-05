from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, InputRequired

class solicitudClinicaDto(FlaskForm):
    email = StringField('email',
                       validators=[DataRequired("Rellene este campo "), Email("Ingrese un email valido")])
    nombreC = StringField('nombreC',
                         validators=[DataRequired("Rellene este campo"), Length(min=2, max=20, message="El nombre debe tener minimo 2 caracteres y maximo 20 caracteres")])
    ciudadC = SelectField('ciudadC', 
                         coerce=str, validators=[DataRequired("Rellene este campo")])
    direccionC = StringField('direccionC', 
                            validators=[DataRequired("Rellene este campo"), Length(min=8, max=30, message="La direccion debe tener minimo 8 caracteres y maximo 30 caracteres")])
    submit = SubmitField('Enviar Solicitud')