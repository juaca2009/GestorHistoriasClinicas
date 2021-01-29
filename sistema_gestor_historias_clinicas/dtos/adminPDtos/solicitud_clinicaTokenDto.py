from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class solicitud_clinicaTokenDto(FlaskForm):
    nombreAc = StringField('nombreAc',
                          validators=[DataRequired("Rellene este campo"), Length(min=2, max=20, message="El nombre debe tener minimo 2 caracteres y maximo 20 caracteres")])
    apellidosAc = StringField('apellidosAc',
                          validators=[DataRequired("Rellene este campo"), Length(min=2, max=20, message="El nombre debe tener minimo 2 caracteres y maximo 20 caracteres")])
    documentoAc = StringField('documentoAc',
                          validators=[DataRequired("Rellene este campo"), Length(min=2, max=20, message="Ingrese un numero valido")])
    TdocumentoAc = SelectField('tipoDocumento', 
                              coerce=str, validators=[DataRequired("Rellene este campo")])
    email = StringField('email',
                       validators=[DataRequired("Rellene este campo "), Email("Ingrese un email valido")])
    telefonoAc = StringField('telefonoAc',
                          validators=[DataRequired("Rellene este campo"), Length(min=7, max=10, message="Ingrese un numero de telefono/celular valido")])
    contrasenaAc = StringField('contrasenaAc',
                          validators=[DataRequired("Rellene este campo"), Length(min=5, max=10, message="La contrasena debe tener minimo 5 caracteres y maximo 10 caracteres")])
    submit = SubmitField('Registrar Administrador Clinico')
    
    def validate_documentoAc(self, documentoAc):
        docu = str(documentoAc.data)
        if docu.isdigit() == False:
            raise ValidationError('Ingrese un numero de documento valido')
    
    def validate_telefonoAc(self, telefonoAc):
        tele = str(telefonoAc.data)
        if tele.isdigit() == False:
            raise ValidationError('Ingrese un numero de telefono/celular que sea valido')