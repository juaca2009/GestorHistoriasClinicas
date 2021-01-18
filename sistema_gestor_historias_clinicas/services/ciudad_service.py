from repository.ciudadRepository import ciudadRepository
from dominios.ciudad import ciudad

class ciudad_service():
    def __init__(self):
        self.__ciuRepo = ciudadRepository()

    def obtener_Tciudades(self):
        """
        funcion encargada de devolver una lista de tuplas de la forma (nombre ciudad, ciudad-departamento)
        para se usado en los dtos correspondientes
        SALIDAS: tuplas de la forma (nombre ciudad, ciudad-departamento)
        """
        salida = self.__ciuRepo.obtener_ciudades()
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