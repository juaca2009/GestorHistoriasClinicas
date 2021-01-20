from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from flask_login import current_user, login_required
from app import app
from services.adminP_servicie import adminP_servicie
from services.ciudad_service import ciudad_service
from services.tipoDocumento_service import tipoDocumento_servicie
from dtos.adminPDtos.agregar_adimPDto import agregar_adimPDto

admin_vista = Blueprint('admin_vista', __name__)

service_adminP = adminP_servicie()
service_ciudad = ciudad_service()
service_tdocumento = tipoDocumento_servicie()

@app.route("/admin/admins", methods = ["GET", "POST"])
@login_required
def adminAdmin():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    admins = service_adminP.obtener_administradores(session['_user_id'])
    return render_template("adminP/adminP_admin.html", titulo='Admin Sistema', admins=admins)




@app.route("/admin/agregarAdmin", methods = ["GET", "POST"])
@login_required
def adminAgregar():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    form = agregar_adimPDto()
    ciudades = service_ciudad.obtener_Tciudades()
    Tdocumento = service_tdocumento.obtener_Tdocumento()
    form.ciudadAp.choices = ciudades
    form.TdocumentoAp.choices = Tdocumento
    if form.validate_on_submit():
        if form.verificar_nroDocumento():
            bandera = service_adminP.agregar_adminP(form.nombreAp.data, form.apellidosAp.data, form.documentoAp.data, form.TdocumentoAp.data, form.email.data, form.telefonoAp.data, form.ciudadAp.data, form.contrasenaAp.data)
            if bandera[0] == 1:
                flash(f'Se ha registrado a {form.nombreAp.data}  {form.apellidosAp.data} satisfactoriamente.', 'success')
                return redirect(url_for('adminAdmin'))
            elif bandera[0] == 0:
                flash(f'El correo ya se encuentra registrado', 'danger')
            else:
                flash(f'Esa persona ya se encuentra registrada en el sistema como administrador general.', 'danger')
        else:
            flash(f'Ingrese un numero de documento valido.', 'danger')
    return render_template("adminP/adminP_agregarAdmin.html", titulo='Admin Sistema', form=form)





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