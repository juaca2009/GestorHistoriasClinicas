from repository.home_repository import home_repository

class home_service():
    def __init__(self):
        self.__HomeRepo = home_repository()

    def obtener_Tciudades(self):
        salida = self.__HomeRepo.obtener_ciudades()
        ciudades_dept = list()
        for i in salida:
            temp = i['nombre']+", "+i['departamentos.nombre']
            ciudades_dept.append(temp)
        return ciudades_dept
