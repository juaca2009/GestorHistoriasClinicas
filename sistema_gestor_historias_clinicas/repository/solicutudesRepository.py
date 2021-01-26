import pymysql
from db_config import mysql 
from dominios.solicitudes import solicitudes

class solicitudesRepsitory(solicitudes):
    def __init__(self):
        self.__conexion = mysql.connect()

    def insertar_solicitudC(self, _nombre, _direccion, _ciudad, _correo):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select insertar_solicitudC(%s, %s, %s, %s)
            """,
            (_nombre, _direccion, _ciudad, _correo)
        )
        salida = cursor.fetchall()
        self.__conexion.commit()
        cursor.close()
        return salida

    def obtener_solicitudes(self):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select id, solicitudes.nombre, direccion, ciudad.nombre from solicitudes inner join ciudad on (solicitudes.cod_postal = ciudad.codigo_postal) 
            """
        )
        salida = cursor.fetchall()
        cursor.close()
        return salida