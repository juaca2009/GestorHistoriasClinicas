from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class agregar_adimPDto(FlaskForm):
    nombreAp = StringField('nombreAp',
                          validators=[DataRequired("Rellene este campo"), Length(min=2, max=20, message="El nombre debe tener minimo 2 caracteres y maximo 20 caracteres")])
    apellidosAp = StringField('apellidosAp',
                          validators=[DataRequired("Rellene este campo"), Length(min=2, max=20, message="El nombre debe tener minimo 2 caracteres y maximo 20 caracteres")])
    documentoAp = StringField('documentoAp',
                          validators=[DataRequired("Rellene este campo"), Length(min=2, max=20, message="Ingrese un numero valido")])
    TdocumentoAp = SelectField('tipoDocumento', 
                              coerce=str, validators=[DataRequired("Rellene este campo")])
    email = StringField('email',
                       validators=[DataRequired("Rellene este campo "), Email("Ingrese un email valido")])
    telefonoAp = StringField('telefonoAp',
                          validators=[DataRequired("Rellene este campo"), Length(min=7, max=10, message="Ingrese un numero de telefono/celular valido")])
    ciudadAp = SelectField('ciudadAp', 
                         coerce=str, validators=[DataRequired("Rellene este campo")])
    contrasenaAp = StringField('contrasenaAp',
                          validators=[DataRequired("Rellene este campo"), Length(min=5, max=10, message="La contrasena debe tener minimo 5 caracteres y maximo 10 caracteres")])
    submit = SubmitField('Registrar Administrador')

    def verificar_nroDocumento(self):
        docu = str(self.documentoAp.data)
        print(docu)
        return docu.isdigit()