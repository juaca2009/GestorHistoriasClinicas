from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class actualizar_adminPDto(FlaskForm):
    nombreAp = StringField('nombreAp')
    apellidosAp = StringField('apellidosAp')
    documentoAp = StringField('documentoAp')
    email = StringField('email',
                       validators=[DataRequired("Rellene este campo "), Email("Ingrese un email valido")])
    telefonoAp = StringField('telefonoAp',
                            validators=[DataRequired("Rellene este campo"), Length(min=7, max=10, message="Ingrese un numero de telefono/celular valido")])
    ciudadAp = SelectField('ciudadAp', 
                         coerce=str, validators=[DataRequired("Rellene este campo")])
    submit = SubmitField('Actualizar Administrador')

    def validate_telefonoAp(self, telefonoAp):
        tele = str(telefonoAp.data)
        if tele.isdigit() == False:
            raise ValidationError('Ingrese un numero de telefono/celular que sea valido')