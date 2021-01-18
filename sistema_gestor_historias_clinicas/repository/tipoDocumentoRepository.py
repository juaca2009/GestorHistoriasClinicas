import pymysql
from db_config import mysql 
from dominios.solicitudes import solicitudes

class tipoDocumentoRepository(solicitudes):
    def __init__(self):
        self.__conexion = mysql.connect()

    def obtener_tipos(self):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select nombre from tipo_documento
            """
        )
        salida = cursor.fetchall()
        cursor.close()
        return salida 