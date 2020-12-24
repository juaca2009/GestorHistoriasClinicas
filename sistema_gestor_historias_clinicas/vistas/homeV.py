from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from app import app

home_vista = Blueprint('home_vista', __name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/inicioSesion", methods = ["GET", "POST"])
def inicio_sesion():
    return render_template("login.html")


@app.route("/registroClinico", methods = ["GET", "POST"])
def registro_clinico():
    return render_template("solicitud_clinica.html")