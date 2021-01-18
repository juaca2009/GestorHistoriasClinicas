from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from flask_login import current_user, login_required
from app import app

admin_vista = Blueprint('admin_vista', __name__)

@app.route("/admin/admins", methods = ["GET", "POST"])
@login_required
def adminAdmin():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_admin.html", titulo='Admin Sistema')

@app.route("/admin/clinicas", methods = ["GET", "POST"])
@login_required
def adminClinicas():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_clinicas.html", titulo='Admin Sistema')

@app.route("/admin/solicitudesClinicas", methods = ["GET", "POST"])
@login_required
def adminSolicitudesClinicas():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_solicitudes.html", titulo='Admin Sistema')

@app.route("/admin/admins/eliminar", methods = ["GET", "POST"])
@login_required
def adminAdminDel():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_adminDel.html", titulo='Admin Sistema')

@app.route("/admin/admins/actualizar", methods = ["GET", "POST"])
@login_required
def adminAdminUp():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_adminUp.html", titulo='Admin Sistema')

@app.route("/admin/admins/informacion", methods = ["GET", "POST"])
@login_required
def adminAdmininfo():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_adminInfo.html", titulo='Admin Sistema')

@app.route("/admin/clinicas/informacion", methods = ["GET", "POST"])
@login_required
def adminCliniasInfo():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_clinicasInfo.html", titulo='Admin Sistema')