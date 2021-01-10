from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from app import app

admin_vista = Blueprint('admin_vista', __name__)

@app.route("/admin/admins", methods = ["GET", "POST"])
def adminAdmin():
    return render_template("adminP_admin.html", titulo='Admin Sistema')

@app.route("/admin/clinicas", methods = ["GET", "POST"])
def adminClinicas():
    return render_template("adminP_clinicas.html", titulo='Admin Sistema')

@app.route("/admin/solicitudesClinicas", methods = ["GET", "POST"])
def adminSolicitudesClinicas():
    return render_template("adminP_solicitudes.html", titulo='Admin Sistema')