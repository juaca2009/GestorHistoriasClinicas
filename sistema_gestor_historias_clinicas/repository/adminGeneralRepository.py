import pymysql
from db_config import mysql 
from dominios.administrador_general import administrador_general

class administradorGeneralRepository(administrador_general):
    def __init__(self):
        self.__conexion = mysql.connect()



    def obtener_administrador(self, _id):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select nro_documento, administrador_general.nombre, apellidos, ciudad.nombre, correo, telefono from administrador_general inner join ciudad on (administrador_general.cod_postal = ciudad.codigo_postal) where nro_documento = %s
            """,
            (_id)
        )
        salida = cursor.fetchall()
        cursor.close()
        return salida[0]

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

    def agregar_administrador(self, _nombre, _apellidos, _documento, _tdocumento, _email, _telefono, _ciudad, _contrasena):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select insertar_adminP(%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (_documento, _tdocumento, _nombre, _apellidos, _email, _telefono, _ciudad, _contrasena)
        )
        salida = cursor.fetchall()
        self.__conexion.commit()
        cursor.close()
        return salida


    def eliminar_administrador(self, _id):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            delete from administrador_general where nro_documento = %s 
            """,
            (_id)
        )
        self.__conexion.commit()
        cursor.close()

    def actualizar_administrador(self, _id, _ciudad, _correo, _telefono):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select actualizar_adminG(%s, %s, %s, %s)
            """,
            (_id, _correo, _telefono, _ciudad)
        )
        salida = cursor.fetchall()
        self.__conexion.commit()
        cursor.close()
        return salida

    def crear_clinica(self, _nombre, _ciudad):
        cursor = self.__conexion.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            select insertar_clinica(%s, %s)
            """,
            (_nombre, _ciudad)
        )
        salida = cursor.fetchall()
        cursor.close()
        return salida[0]