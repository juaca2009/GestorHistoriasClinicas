import pymysql
from db_config import mysql 
from dominios.administrador_clinica import administrador_clinica

class administradorClinicoRepository(administrador_clinica):
    def __init__(self):
        self.__conexion = mysql.connect()

    def agregar_administradorC(self, _nombre, _apellidos, _documento, _tdocumento, _email, _telefono, _clinica, _contrasena):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select insertar_adminC(%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (_nombre, _apellidos, _documento, _tdocumento, _email, _telefono, _clinica, _contrasena)
        )
        salida = cursor.fetchall()
        self.__conexion.commit()
        cursor.close()
        return salida