import pymysql
from db_config import mysql 
from dominios.administrador_clinica import administrador_clinica

class administradorClinicoRepository(administrador_clinica):
    def __init__(self):
        self.__conexion = mysql.connect()