from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from flask_login import current_user
from app import app

admin_vista = Blueprint('admin_vista', __name__)

@app.route("/admin/admins", methods = ["GET", "POST"])
def adminAdmin():
    return render_template("adminP/adminP_admin.html", titulo='Admin Sistema')

@app.route("/admin/clinicas", methods = ["GET", "POST"])
def adminClinicas():
    return render_template("adminP/adminP_clinicas.html", titulo='Admin Sistema')

@app.route("/admin/solicitudesClinicas", methods = ["GET", "POST"])
def adminSolicitudesClinicas():
    return render_template("adminP/adminP_solicitudes.html", titulo='Admin Sistema')

@app.route("/admin/admins/eliminar", methods = ["GET", "POST"])
def adminAdminDel():
    return render_template("adminP/adminP_adminDel.html", titulo='Admin Sistema')

@app.route("/admin/admins/actualizar", methods = ["GET", "POST"])
def adminAdminUp():
    return render_template("adminP/adminP_adminUp.html", titulo='Admin Sistema')

@app.route("/admin/admins/informacion", methods = ["GET", "POST"])
def adminAdmininfo():
    return render_template("adminP/adminP_adminInfo.html", titulo='Admin Sistema')

@app.route("/admin/clinicas/informacion", methods = ["GET", "POST"])
def adminCliniasInfo():
    return render_template("adminP/adminP_clinicasInfo.html", titulo='Admin Sistema')