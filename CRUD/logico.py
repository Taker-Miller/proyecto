import mysql.connector
from mysql.connector import Error

def crear_conexion():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='gestion_tickets'
    )

def validar_usuario(nombre_usuario, contrasena):
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT IDUsuario FROM Usuario WHERE Nombre=%s AND Contrasena=%s", (nombre_usuario, contrasena))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuario
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def registrar_usuario(nombre_usuario, correo, contrasena, tipo):
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuario (Nombre, Correo, Contrasena, Tipo) VALUES (%s, %s, %s, %s)", (nombre_usuario, correo, contrasena, tipo))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error al registrar usuario: {e}")
        return False

def registrar_incidencia(titulo, descripcion, estado, fecha_creacion, fecha_actualizacion, id_usuario):
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Incidencia (Titulo, Descripcion, Estado, FechaCreacion, FechaActualizacion, IDUsuario) VALUES (%s, %s, %s, %s, %s, %s)", (titulo, descripcion, estado, fecha_creacion, fecha_actualizacion, id_usuario))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error al registrar incidencia: {e}")
        return False

def obtener_todas_las_incidencias():
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Incidencia")
        incidencias = cursor.fetchall()
        cursor.close()
        conn.close()
        return incidencias
    except Error as e:
        print(f"Error al obtener incidencias: {e}")
        return []

def actualizar_incidencia(id_incidencia, titulo, descripcion, estado, fecha_actualizacion):
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("UPDATE Incidencia SET Titulo=%s, Descripcion=%s, Estado=%s, FechaActualizacion=%s WHERE IDIncidencia=%s", (titulo, descripcion, estado, fecha_actualizacion, id_incidencia))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error al actualizar incidencia: {e}")
        return False

def borrar_incidencia(id_incidencia):
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Incidencia WHERE IDIncidencia=%s", (id_incidencia,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error al borrar incidencia: {e}")
        return False

def registrar_asignacion(id_incidencia, id_tecnico, fecha_asignacion):
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Asignacion (IDIncidencia, IDTecnico, FechaAsignacion) VALUES (%s, %s, %s)", (id_incidencia, id_tecnico, fecha_asignacion))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Error as e:
        print(f"Error al registrar asignación: {e}")
        return False

def obtener_todas_las_asignaciones():
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Asignacion")
        asignaciones = cursor.fetchall()
        cursor.close()
        conn.close()
        return asignaciones
    except Error as e:
        print(f"Error al obtener asignaciones: {e}")
        return []
