from repository.solicutudesRepository import solicitudesRepsitory


class home_service():
    def __init__(self):
        self.__solRepo = solicitudesRepsitory()

    def insertar_solicitudC(self, _nombre, _direccion, _ciudad, _correo):
        salida = self.__solRepo.insertar_solicitudC(_nombre, _direccion, _ciudad, _correo)
        return list(salida[0].values())