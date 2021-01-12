import pymysql
from db_config import mysql 
from dominios.ciudad import ciudad

class ciudadRepository(ciudad):
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