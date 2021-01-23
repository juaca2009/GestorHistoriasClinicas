from flask import Flask, render_template, request, redirect, session, g, url_for, flash, Blueprint
from flask_login import current_user, login_required
from app import app
from services.adminP_servicie import adminP_servicie
from services.ciudad_service import ciudad_service
from services.tipoDocumento_service import tipoDocumento_servicie
from dtos.adminPDtos.agregar_adimPDto import agregar_adimPDto
from dtos.adminPDtos.eliminar_adminPDto import eliminar_adminPDto
from dtos.adminPDtos.actualizar_adminPDto import actualizar_adminPDto
from dtos.adminPDtos.info_adminPDto import info_adminPDto

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



@app.route("/admin/admins/eliminar/<int:id>", methods = ["GET", "POST"])
@login_required
def adminAdminDel(id):
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    form = eliminar_adminPDto()
    info_admin = service_adminP.obtener_adminP(id)
    if form.validate_on_submit():
        service_adminP.eliminar_adminP(id)
        nombre = info_admin['nombre']
        apellidos = info_admin['apellidos']
        flash(f'Se ha Eliminado a {nombre}  {apellidos} satisfactoriamente.', 'warning')
        return redirect(url_for('adminAdmin'))
    return render_template("adminP/adminP_adminDel.html", titulo='Admin Sistema', form=form, info=info_admin)




@app.route("/admin/admins/actualizar/<int:id>", methods = ["GET", "POST"])
@login_required
def adminAdminUp(id):
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    ciudades = service_ciudad.obtener_Tciudades()
    form = actualizar_adminPDto()
    info_admin = service_adminP.obtener_adminP(id)
    form.ciudadAp.choices = ciudades
   
    if form.validate_on_submit():
        print(form.telefonoAp.data)
        bandera = service_adminP.actualizar_adminP(info_admin['nro_documento'], form.ciudadAp.data, form.email.data, form.telefonoAp.data)
        if bandera[0] == 1:
            nombre = info_admin['nombre']
            apellidos = info_admin['apellidos']
            flash(f'Se ha actualizado a {nombre}  {apellidos} satisfactoriamente.', 'success')
            return redirect(url_for('adminAdmin'))
        else:
            flash(f'El correo ya se encuentra registrado', 'danger')
    elif request.method == 'GET':
        form.ciudadAp.data = info_admin['ciudad.nombre']
        form.email.data = info_admin['correo']
        form.telefonoAp.data = info_admin['telefono']
    return render_template("adminP/adminP_adminUp.html", titulo='Admin Sistema', form=form, info=info_admin)




@app.route("/admin/admins/informacion/<int:id>", methods = ["GET", "POST"])
@login_required
def adminAdmininfo(id):
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    form = info_adminPDto()
    info_admin = service_adminP.obtener_adminP(id)
    return render_template("adminP/adminP_adminInfo.html", titulo='Admin Sistema', info=info_admin, form=form)



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
        bandera = service_adminP.agregar_adminP(form.nombreAp.data, form.apellidosAp.data, form.documentoAp.data, form.TdocumentoAp.data, form.email.data, form.telefonoAp.data, form.ciudadAp.data, form.contrasenaAp.data)
        if bandera[0] == 1:
            flash(f'Se ha registrado a {form.nombreAp.data}  {form.apellidosAp.data} satisfactoriamente.', 'success')
            return redirect(url_for('adminAdmin'))
        elif bandera[0] == 0:
            flash(f'El correo ya se encuentra registrado', 'danger')
        else:
            flash(f'Esa persona ya se encuentra registrada en el sistema como administrador general.', 'danger')
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

@app.route("/admin/clinicas/informacion", methods = ["GET", "POST"])
@login_required
def adminCliniasInfo():
    if session['tipo_cuenta'] != 'aGeneral':
        return redirect(url_for('home'))
    return render_template("adminP/adminP_clinicasInfo.html", titulo='Admin Sistema')