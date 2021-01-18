import pymysql
from db_config import mysql 
from dominios.administrador_general import administrador_general

class administradorGeneralRepository(administrador_general):
    def __init__(self):
        self.__conexion = mysql.connect()

    def obtener_administradores(self):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select nro_documento, administrador_general.nombre, apellidos, ciudad.nombre from administrador_general inner join ciudad on (administrador_general.cod_postal = ciudad.codigo_postal)
            """
        )
        salida = cursor.fetchall()
        cursor.close()
        return salida 