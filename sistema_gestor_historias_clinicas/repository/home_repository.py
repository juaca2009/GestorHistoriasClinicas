import pymysql
from db_config import mysql 

class home_repository():
    def __init__(self):
        self.__conexion = mysql.connect()

    def obtener_ciudades(self):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select ciudad.nombre, departamentos.nombre from ciudad inner join departamentos on (ciudad.id_departamento = departamentos.id)
            """
        )
        salida = cursor.fetchall()
        cursor.close()
        return salida 

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