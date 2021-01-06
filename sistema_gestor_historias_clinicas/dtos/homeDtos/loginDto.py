from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class loginDto(FlaskForm):
    email = StringField('email',
                       validators=[DataRequired("Rellene este campo "), Email("Ingrese un email valido")])
    contra = StringField('contraseña',
                       validators=[DataRequired("Rellene este campo ")])
    tipoL = SelectField('ciudadC', 
                         choices=[('paciente',"Paciente"),('medico',"Medico"), ('aClinico', "Administrador Clinico"), ('aSistema', "Administrador del Sistema")], 
                         validators=[DataRequired("Rellene este campo")])