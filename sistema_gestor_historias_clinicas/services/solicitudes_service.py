from repository.solicutudesRepository import solicitudesRepsitory
from dominios.solicitudes import solicitudes
from itsdangerous import TimedJSONWebSignatureSerializer as token
from app import app

class solicitudes_service():
    def __init__(self):
        self.__solRepo = solicitudesRepsitory()

    def obtener_solicitud(self, _id):
        return self.__solRepo.obtener_solicitud(_id)

    def obtener_solicitudes(self):
        salida = self.__solRepo.obtener_solicitudes()
        return salida

    def insertar_solicitudC(self, _nombre, _direccion, _ciudad, _correo):
        salida = self.__solRepo.insertar_solicitudC(_nombre, _direccion, _ciudad, _correo)
        return list(salida[0].values())

    def eliminar_solicitud(self, _id):
        self.__solRepo.eliminar_solicitud(_id)

    def actualizar_estadoS(self, _id):
        self.__solRepo.actualizar_estado(_id)

    def generar_token(self, _idS, _idC):
        s = token.serializer(app.config['SECRET_KEY'], 86400)  #duracion del token 24 horas = 86400 segundos
        return s.dumps({'solicitud_id': _idS, 'clinica_id': _idC}).decode('utf-8')

    def verificar_token(self, _token):
        s = token.serializer(app.config['SECRET_KEY'])
        try:
            id_solicitud = s.loads(_token)['solicitud_id']
            id_clinica = s.loads(_token)['clinica_id']
        except:
            return None
        temp = list()
        temp.append(id_solicitud)
        temp.append(id_clinica)
        return temp