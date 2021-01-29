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

    def obtener_idTipo(self, _nombre):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select id from tipo_documento where nombre = %s;
            """,
            (_nombre)
        )
        salida = cursor.fetchall()
        cursor.close()
        return salida[0]