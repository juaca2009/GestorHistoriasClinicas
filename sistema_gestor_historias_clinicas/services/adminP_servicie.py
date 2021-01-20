from repository.adminGeneralRepository import administradorGeneralRepository
from dominios.administrador_general import administrador_general
from app import encriptador

class adminP_servicie():
    def __init__(self):
        self.__adminPRepo = administradorGeneralRepository()

    def obtener_administradores(self, _id):
        salida = self.__adminPRepo.obtener_administradores()
        contador = 0
        bandera = False
        while bandera != True:
            if salida[contador]['nro_documento'] == _id:
                bandera = True
                salida.pop(contador)
            contador = contador + 1
        return salida


    def agregar_adminP(self, _nombre, _apellidos, _documento, _tdocumento, _email, _telefono, _ciudad, _contrasena):
        _contrasena = encriptador.generate_password_hash(_contrasena).decode('utf-8')
        salida = self.__adminPRepo.agregar_administrador(_nombre, _apellidos, _documento, _tdocumento, _email, _telefono, _ciudad, _contrasena)
        return list(salida[0].values())