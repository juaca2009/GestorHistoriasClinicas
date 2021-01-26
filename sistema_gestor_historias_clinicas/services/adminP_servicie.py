from repository.adminGeneralRepository import administradorGeneralRepository
from repository.solicutudesRepository import solicitudesRepsitory
from dominios.administrador_general import administrador_general
from app import encriptador

class adminP_servicie():
    def __init__(self):
        self.__adminPRepo = administradorGeneralRepository()
        self.__solRepo = solicitudesRepsitory()

    def obtener_adminP(self, _id):
        return self.__adminPRepo.obtener_administrador(_id)

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

    
    def eliminar_adminP(self, _id):
        self.__adminPRepo.eliminar_administrador(_id)

    def actualizar_adminP(self, _id, _ciudad, _correo, _telefono):
        salida = self.__adminPRepo.actualizar_administrador(_id, _ciudad, _correo, _telefono)
        return list(salida[0].values())

    def obtener_solicitudes(self):
        salida = self.__solRepo.obtener_solicitudes()
        return salida

    