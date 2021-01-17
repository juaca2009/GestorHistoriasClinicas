import pymysql
from db_config import mysql 
from dominios.paciente import paciente

class pacienteRepository(paciente):
    def __init__(self):
        self.__conexion = mysql.connect()