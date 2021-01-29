from repository.adminClinicoRepository import administradorClinicoRepository
from dominios.administrador_clinica import administrador_clinica
from app import encriptador

class adminC_service():
    def __init__(self):
        self.__adminCRepo = administradorClinicoRepository()
    
    def agregar_adminC(self, _nombre, _apellidos, _documento, _tdocumento, _email, _telefono, _clinica, _contrasena):
        _contrasena = encriptador.generate_password_hash(_contrasena).decode('utf-8')
        salida = self.__adminCRepo.agregar_administradorC(_nombre, _apellidos, _documento, _tdocumento, _email, _telefono, _clinica, _contrasena)
        return list(salida[0].values())