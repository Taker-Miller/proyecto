import tkinter as tk
from tkinter import messagebox
from logica import registrar_usuario

def crear_interfaz_registro(root, crear_interfaz_inicio_sesion, crear_interfaz_principal):
    # Limpiar la ventana actual y preparar la interfaz de registro
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Registro - Sistema de Mesa de Ayuda")
    root.geometry("300x400")  # Aumentado para acomodar los nuevos botones

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="Nombre de usuario:").pack()
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)

    tk.Label(frame, text="Correo electrónico:").pack()
    email_entry = tk.Entry(frame)
    email_entry.pack(pady=5)

    tk.Label(frame, text="Contraseña:").pack()
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=5)

    tk.Label(frame, text="Tipo de usuario:").pack()
    tipo_usuario = tk.StringVar(root)
    tipo_usuario.set("Usuario")
    tipo_usuario_menu = tk.OptionMenu(frame, tipo_usuario, "Administrador", "Técnico", "Usuario")
    tipo_usuario_menu.pack(pady=5)

    tk.Button(frame, text="Registrar usuario", command=lambda: manejar_registro(username_entry.get(), email_entry.get(), password_entry.get(), tipo_usuario.get(), root, crear_interfaz_inicio_sesion)).pack(pady=10)
    tk.Button(frame, text="Regresar", command=crear_interfaz_inicio_sesion).pack(pady=10)

def manejar_registro(nombre_usuario, correo, contrasena, tipo, root, crear_interfaz_inicio_sesion):
    if not nombre_usuario or not correo or not contrasena or not tipo:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    
    if "@" not in correo:
        messagebox.showerror("Error", "El correo electrónico debe contener '@'.")
        return

    if registrar_usuario(nombre_usuario, correo, contrasena, tipo):
        messagebox.showinfo("Registro", "Usuario registrado exitosamente.")
        crear_interfaz_inicio_sesion()
    else:
        messagebox.showerror("Error", "No se pudo registrar el usuario.")
