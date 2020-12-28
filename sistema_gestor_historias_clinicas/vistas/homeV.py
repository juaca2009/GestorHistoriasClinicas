from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from app import app
from services.home_service import home_service

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
    ciudades = services_home.obtener_Tciudades()
    return render_template("solicitud_clinica.html", titulo='Registro Clinico', ciudad=ciudades)