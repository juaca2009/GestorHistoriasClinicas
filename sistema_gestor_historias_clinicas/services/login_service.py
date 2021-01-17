from main import login_manager
from dominios.administrador_clinica import administrador_clinica
from dominios.administrador_general import administrador_general
from dominios.paciente import paciente
from dominios.medicos import medicos
from repository.adminClinicoRepository import administradorClinicoRepository
from repository.adminGeneralRepository import administradorGeneralRepository
from repository.medicosRepository import medicosRepository
from repository.pacienteRepository import pacienteRepository

@login_manager.user_loader
def cargar_usuario(nro_documento, tipo):
    if tipo == 'paciente':
        pacient = paciente()
        return pacient.query.get.(int(nro_documento))
    elif tipo == 'medico':
        medic = medicos()
        return medic.query.get.(int(nro_documento))
    elif tipo == 'aClinico':
        aclinico = administrador_clinica()
        return aclinico.query.get.(int(nro_documento))
    else:
        ageneral = administrador_general()
        return ageneral.query.get.(int(nro_documento))