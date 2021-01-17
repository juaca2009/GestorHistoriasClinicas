import pymysql
from db_config import mysql 
from dominios.medicos import medicos

class medicosRepository(medicos):
    def __init__(self):
        self.__conexion = mysql.connect()