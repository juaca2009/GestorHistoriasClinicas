from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from flask_login import login_user, current_user, logout_user
from app import app
from services.home_service import home_service
from services.ciudad_service import ciudad_service
from services.login_service import login_servicie
from dtos.homeDtos.solicitudClinicaDto import solicitudClinicaDto
from dtos.homeDtos.loginDto import loginDto
from app import login_manager

home_vista = Blueprint('home_vista', __name__)

services_home = home_service()
services_login = login_servicie()
services_ciudad = ciudad_service()


@login_manager.user_loader
def cargar_usuario(nro_documento):
    if session['tipo_cuenta'] == 'paciente':
        return services_login.obtener_paciente_id(nro_documento)
    elif session['tipo_cuenta'] == 'medico':
        return services_login.obtener_medico_id(nro_documento)
    elif session['tipo_cuenta'] == 'aClinico':
        return services_login.obtener_aClinico_id(nro_documento)
    else:
        return services_login.obtener_aGeneral_id(nro_documento)






@app.route("/", methods = ["GET", "POST"])
def home():
    if current_user.is_authenticated == False:
        session['tipo_cuenta'] = 'None'
    return render_template("home/home.html", bandLogin="", tipoS=session['tipo_cuenta'])


@app.route("/inicioSesion", methods = ["GET", "POST"])
def inicio_sesion():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = loginDto()
    if form.validate_on_submit():
        if form.tipoL.data == 'paciente':
            session['tipo_cuenta'] = 'paciente'
            paciente = services_login.obtener_paciente(form.email.data)
            if paciente and paciente.contrasena == form.contra.data:
                login_user(paciente)
                return redirect(url_for('home'))
            else:
                flash(f'Correo o contraseña erroneos, revise su informacion', 'danger')
        elif form.tipoL.data == 'medico':
            session['tipo_cuenta'] = 'medico'
            medico = services_login.obtener_medico(form.email.data)
            if medico and medico.contrasena == form.contra.data:
                login_user(medico)
                return redirect(url_for('home'))
            else:
                flash(f'Correo o contraseña erroneos, revise su informacion', 'danger')
        elif form.tipoL.data == 'aClinico':
            session['tipo_cuenta'] = 'aClinico'
            aclinico = services_login.obtener_aclinico(form.email.data)
            if aclinico and aclinico.contrasena == form.contra.data:
                login_user(aclinico)
                return redirect(url_for('home'))
            else:
                flash(f'Correo o contraseña erroneos, revise su informacion', 'danger')
        else:
            session['tipo_cuenta'] = 'aGeneral'
            ageneral = services_login.obtener_ageneral(form.email.data)
            if ageneral and ageneral.contrasena == form.contra.data:
                print(type(ageneral))
                login_user(ageneral)
                return redirect(url_for('adminAdmin'))
            else:
                flash(f'Correo o contraseña erroneos, revise su informacion', 'danger')
    return render_template("home/login.html", titulo='Inicio Sesion', form=form, bandLogin="1")


@app.route("/cerrarSesion")
def cerrarSesion():
    logout_user()
    return redirect(url_for('inicio_sesion'))


@app.route("/registroClinico", methods = ["GET", "POST"])
def registro_clinico():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = solicitudClinicaDto()
    ciudades = services_ciudad.obtener_Tciudades()
    form.ciudadC.choices = ciudades #asignacion de tuplas para el form dinamico select
    if form.validate_on_submit():
        bandera_creacion = services_home.insertar_solicitudC(form.nombreC.data, form.direccionC.data, form.ciudadC.data, form.email.data)
        if bandera_creacion[0] == 1:
            flash(f'La solicitud para {form.nombreC.data} ha sido enviada. Revise su correo para mas instrucciones.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'La solicitud para {form.nombreC.data} ya ha sido enviada o la clinica ya esta registrada.', 'danger')
    return render_template("home/solicitud_clinica.html", titulo='Registro Clinico', form=form, bandLogin="")