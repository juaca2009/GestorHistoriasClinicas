import pymysql
from db_config import mysql 
from dominios.administrador_general import administrador_general

class administradorGeneralRepository(administrador_general):
    def __init__(self):
        self.__conexion = mysql.connect()