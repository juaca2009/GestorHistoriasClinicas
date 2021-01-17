from repository.adminClinicoRepository import administradorClinicoRepository
from repository.adminGeneralRepository import administradorGeneralRepository
from repository.medicosRepository import medicosRepository
from repository.pacienteRepository import pacienteRepository



class login_servicie():
    def __init__(self):
        self.__pacienteRepo = pacienteRepository()
        self.__medicoRepo = medicosRepository()
        self.__aclinicoRepo = administradorClinicoRepository()
        self.__ageneralRepo = administradorGeneralRepository()
    
    def obtener_paciente(self, _email):
        return self.__pacienteRepo.query.filter_by(correo=_email).first()

    def obtener_medico(self, _email):
        return self.__medicoRepo.query.filter_by(correo=_email).first()

    def obtener_aclinico(self, _email):
        return self.__aclinicoRepo.query.filter_by(correo=_email).first()

    def obtener_ageneral(self, _email):
        return self.__ageneralRepo.query.filter_by(correo=_email).first()

    def obtener_paciente_id(self, _id):
        return self.__pacienteRepo.query.get(int(_id))
    
    def obtener_medico_id(self, _id):
        return self.__medicoRepo.query.get(int(_id))

    def obtener_aClinico_id(self, _id):
        return self.__aclinicoRepo.query.get(int(_id))

    def obtener_aGeneral_id(self, _id):
        return self.__ageneralRepo.query.get(int(_id))
