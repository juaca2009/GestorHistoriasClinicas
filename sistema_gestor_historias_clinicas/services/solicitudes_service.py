from repository.solicutudesRepository import solicitudesRepsitory
from dominios.solicitudes import solicitudes

class solicitudes_service():
    def __init__(self):
        self.__solRepo = solicitudesRepsitory()

    def obtener_solicitudes(self):
        salida = self.__solRepo.obtener_solicitudes()
        return salida

    def insertar_solicitudC(self, _nombre, _direccion, _ciudad, _correo):
        salida = self.__solRepo.insertar_solicitudC(_nombre, _direccion, _ciudad, _correo)
        return list(salida[0].values())

    def eliminar_solicitud(self, _id):
        self.__solRepo.eliminar_solicitud(_id)