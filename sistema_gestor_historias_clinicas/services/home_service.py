from repository.home_repository import home_repository

class home_service():
    def __init__(self):
        self.__HomeRepo = home_repository()

    def obtener_Tciudades(self):
        """
        funcion encargada de devolver una lista de tuplas de la forma (nombre ciudad, ciudad-departamento)
        para se usado en los dtos correspondientes
        SALIDAS: tuplas de la forma (nombre ciudad, ciudad-departamento)
        """
        salida = self.__HomeRepo.obtener_ciudades()
        ciudades_label = list()
        for i in salida:
            temp = i['nombre']+", "+i['departamentos.nombre'] #formato de nombre ciudad,departamento
            ciudades_label.append(temp)
        grupo_ciudades = list()
        cont = 0
        while cont < len(salida):
            temp = (salida[cont]['nombre'], ciudades_label[cont]) #creacion tuplas
            grupo_ciudades.append(temp)
            cont = cont + 1
        return grupo_ciudades

    def insertar_solicitudC(self, _nombre, _direccion, _ciudad, _correo):
        salida = self.__HomeRepo.insertar_solicitudC(_nombre, _direccion, _ciudad, _correo)
        return list(salida[0].values())