from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class solicitudClinicaDto(FlaskForm):
    email = StringField('email',
                       validators=[DataRequired(), Email()])
    nombreC = StringField('nombreC',
                         validators=[DataRequired(), Length(min=2, max=20)])
    ciudadC = SelectField('ciudadC', 
                         coerce=str, validators=[DataRequired()])
    direccionC = StringField('direccionC', 
                            validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField('Enviar Solicitud')