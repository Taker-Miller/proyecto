import mysql.connector
from mysql.connector import Error

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database=''
    )

def fetch_all(query):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def execute_query(query, params=None):
    conn = create_connection()
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def validar_usuario(nombre_usuario, contraseña):
    query = "SELECT IDUsuario FROM usuario WHERE nombre = %s AND contraseña = %s"
    params = (nombre_usuario, contraseña)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def registrar_usuario(nombre_usuario, correo, contraseña, tipo):
    query = "INSERT INTO usuario (nombre, correo, contraseña, tipo) VALUES (%s, %s, %s, %s)"
    params = (nombre_usuario, correo, contraseña, tipo)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al registrar usuario: {e}")
        return False

def registrar_incidencia(titulo, descripción, estado, fecha_creacion, fecha_actualizacion, id_usuario):
    query = "INSERT INTO incidencia (Titulo, Descripción, Estado, FechaCreacion, FechaActualizacion, IDUsuario) VALUES (%s, %s, %s, %s, %s, %s)"
    params = (titulo, descripción, estado, fecha_creacion, fecha_actualizacion, id_usuario)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al registrar incidencia: {e}")
        return False

def obtener_todas_las_incidencias():
    query = "SELECT * FROM incidencia"
    return fetch_all(query)

def actualizar_incidencia(id_incidencia, titulo, descripción, estado, fecha_actualizacion):
    query = "UPDATE incidencia SET Titulo = %s, Descripción = %s, Estado = %s, FechaActualizacion = %s WHERE IDIncidencia = %s"
    params = (titulo, descripción, estado, fecha_actualizacion, id_incidencia)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al actualizar incidencia: {e}")
        return False

def borrar_incidencia(id_incidencia):
    query = "DELETE FROM incidencia WHERE IDIncidencia = %s"
    params = (id_incidencia,)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al borrar incidencia: {e}")
        return False

def registrar_asignacion(id_incidencia, id_tecnico, fecha_asignacion):
    query = "INSERT INTO asignacion (IDIncidencia, IDTecnico, FechaAsignacion) VALUES (%s, %s, %s)"
    params = (id_incidencia, id_tecnico, fecha_asignacion)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al registrar asignacion: {e}")
        return False

def obtener_todas_las_asignaciones():
    query = "SELECT * FROM asignacion"
    return fetch_all(query)

def obtener_todos_los_usuarios():
    query = "SELECT IDUsuario, Nombre, Correo, Tipo FROM usuario"
    return fetch_all(query)
