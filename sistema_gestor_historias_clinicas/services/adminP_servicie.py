from repository.adminGeneralRepository import administradorGeneralRepository
from dominios.administrador_general import administrador_general

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