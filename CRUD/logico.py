def validar_usuario(user_data):
    errores = {}
    if not user_data['nombre'].strip():
        errores['nombre'] = "El nombre es requerido."
    if not user_data['email'].strip():
        errores['email'] = "El email es requerido."
    if '@' not in user_data['email']:
        errores['email'] = "El email debe contener '@'."
    return errores

def proceso_usuario(user_data):
    datos_procesados = {
        'nombre': user_data['nombre'].strip().title(),
        'email': user_data['email'].strip().lower()
    }
    return datos_procesados
