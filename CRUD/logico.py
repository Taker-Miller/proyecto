import mysql.connector
from mysql.connector import Error

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='ticket'
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
    query = "SELECT IDUsuario, Tipo FROM usuario WHERE nombre = %s AND contraseña = %s"
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

def registrar_incidencia(titulo, descripcion, estado, fecha_creacion, fecha_actualizacion, id_usuario):
    query = "INSERT INTO incidencia (Titulo, Descripción, Estado, FechaCreacion, FechaActualizacion, IDUsuario) VALUES (%s, %s, %s, %s, %s, %s)"
    params = (titulo, descripcion, estado, fecha_creacion, fecha_actualizacion, id_usuario)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al registrar incidencia: {e}")
        return False

def obtener_todas_las_incidencias():
    query = "SELECT * FROM incidencia"
    return fetch_all(query)

def actualizar_incidencia(id_incidencia, titulo, descripcion, estado, fecha_actualizacion):
    query = "UPDATE incidencia SET Titulo = %s, Descripción = %s, Estado = %s, FechaActualizacion = %s WHERE IDIncidencia = %s"
    params = (titulo, descripcion, estado, fecha_actualizacion, id_incidencia)
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

def borrar_asignacion(id_asignacion):
    query = "DELETE FROM asignacion WHERE IDAsignacion = %s"
    params = (id_asignacion,)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al borrar asignación: {e}")
        return False

def obtener_todos_los_usuarios():
    query = "SELECT IDUsuario, Nombre, Correo, Tipo FROM usuario"
    return fetch_all(query)

def borrar_usuario(id_usuario):
    query = "DELETE FROM usuario WHERE IDUsuario = %s"
    params = (id_usuario,)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al borrar usuario: {e}")
        return False

def obtener_todos_los_tecnicos():
    query = "SELECT IDUsuario, Nombre FROM usuario WHERE Tipo = 'Técnico'"
    return fetch_all(query)

def registrar_informe(titulo, contenido, fecha_generacion, id_administrador):
    query = "INSERT INTO informe (Titulo, Contenido, FechaGeneracion, IDAdministrador) VALUES (%s, %s, %s, %s)"
    params = (titulo, contenido, fecha_generacion, id_administrador)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al registrar informe: {e}")
        return False

def obtener_todos_los_informes():
    query = "SELECT * FROM informe"
    return fetch_all(query)

def actualizar_informe(id_informe, titulo, contenido, fecha_generacion):
    query = "UPDATE informe SET Titulo = %s, Contenido = %s, FechaGeneracion = %s WHERE IDInforme = %s"
    params = (titulo, contenido, fecha_generacion, id_informe)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al actualizar informe: {e}")
        return False

def borrar_informe(id_informe):
    query = "DELETE FROM informe WHERE IDInforme = %s"
    params = (id_informe,)
    try:
        execute_query(query, params)
        return True
    except Error as e:
        print(f"Error al borrar informe: {e}")
        return False
