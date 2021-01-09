from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from app import app
from services.home_service import home_service
from dtos.homeDtos.solicitudClinicaDto import solicitudClinicaDto
from dtos.homeDtos.loginDto import loginDto

home_vista = Blueprint('home_vista', __name__)

services_home = home_service()

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html", bandLogin="")


@app.route("/inicioSesion", methods = ["GET", "POST"])
def inicio_sesion():
    form = loginDto()
    if form.validate_on_submit():
        inicio = False
        if inicio == True:
            print("1")
        else:
            flash(f'error', 'danger')
    return render_template("login.html", titulo='Inicio Sesion', form=form, bandLogin="1")


@app.route("/registroClinico", methods = ["GET", "POST"])
def registro_clinico():
    form = solicitudClinicaDto()
    ciudades = services_home.obtener_Tciudades()
    form.ciudadC.choices = ciudades #asignacion de tuplas para el form dinamico select
    if form.validate_on_submit():
        bandera_creacion = services_home.insertar_solicitudC(form.nombreC.data, form.direccionC.data, form.ciudadC.data, form.email.data)
        if bandera_creacion[0] == 1:
            flash(f'La solicitud para {form.nombreC.data} ha sido enviada. Revise su correo para mas instrucciones.', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'La solicitud para {form.nombreC.data} ya ha sido enviada o la clinica ya esta registrada.', 'danger')
    return render_template("solicitud_clinica.html", titulo='Registro Clinico', form=form, bandLogin="")