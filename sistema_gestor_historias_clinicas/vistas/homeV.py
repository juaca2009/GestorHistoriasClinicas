from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from app import app
from services.home_service import home_service
from dtos.homeDtos.solicitudClinicaDto import solicitudClinicaDto

home_vista = Blueprint('home_vista', __name__)

services_home = home_service()

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/inicioSesion", methods = ["GET", "POST"])
def inicio_sesion():
    return render_template("login.html", titulo='Inicio Sesion')


@app.route("/registroClinico", methods = ["GET", "POST"])
def registro_clinico():
    form = solicitudClinicaDto()
    ciudades = services_home.obtener_Tciudades()
    form.ciudadC.choices = ciudades #asignacion de tuplas para el form dinamico select
    if form.validate_on_submit():
        flash(f'La solicitud para {form.nombreC.data} ha sido enviada', 'success')
        return redirect(url_for('home'))
    return render_template("solicitud_clinica.html", titulo='Registro Clinico', form=form)