from repository.tipoDocumentoRepository import tipoDocumentoRepository
from dominios.tipo_documento import tipo_documento

class tipoDocumento_servicie():
    def __init__(self):
        self.__tipDRepo = tipoDocumentoRepository()

    def obtener_Tdocumento(self):
        salida = self.__tipDRepo.obtener_tipos()
        tipos_grupos = list()
        cont = 0
        while cont < len(salida):
            temp = (salida[cont]['nombre'], salida[cont]['nombre'])
            tipos_grupos.append(temp)
            cont = cont + 1
        return tipos_grupos
