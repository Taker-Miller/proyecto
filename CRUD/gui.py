import tkinter as tk
from tkinter import ttk, messagebox
from database import fetch_all, execute_query
from logico import validar_usuario, proceso_usuario

def setup_gui(root):
    root.title("Consultenos")
    root.geometry("800x600")
    root.configure(bg='#f0f0f0')

    main_frame = ttk.Frame(root, padding="10 10 10 10")
    main_frame.pack(expand=True, fill='both', padx=10, pady=10)

    style = ttk.Style()
    style.configure("TButton", font=('Calibri', 12))
    style.configure("TLabel", font=('Calibri', 12))
    style.configure("TEntry", font=('Calibri', 12), padding=5)

    ttk.Label(main_frame, text="ID:").grid(row=0, column=0, sticky=tk.W)
    id_entry = ttk.Entry(main_frame, width=20)
    id_entry.grid(row=0, column=1, sticky=tk.W)

    ttk.Label(main_frame, text="Nombre:").grid(row=1, column=0, sticky=tk.W)
    name_entry = ttk.Entry(main_frame, width=20)
    name_entry.grid(row=1, column=1, sticky=tk.W)

    ttk.Label(main_frame, text="Email:").grid(row=2, column=0, sticky=tk.W)
    email_entry = ttk.Entry(main_frame, width=20)
    email_entry.grid(row=2, column=1, sticky=tk.W)

    load_btn = ttk.Button(main_frame, text="Cargar Usuarios", command=lambda: validate_and_load_data(id_entry, name_entry, email_entry))
    load_btn.grid(row=3, column=0, columnspan=2, pady=10)

    tree_view = ttk.Treeview(main_frame, columns=('id', 'nombre', 'email'), show='headings')
    tree_view.grid(row=4, column=0, columnspan=2, sticky='nsew')
    for col in ('id', 'nombre', 'email'):
        tree_view.heading(col, text=col.capitalize())

    return tree_view

def validate_and_load_data(id_entry, name_entry, email_entry):
    user_data = {
        'nombre': name_entry.get(),
        'email': email_entry.get()
    }
    errores = validar_usuario(user_data)
    if errores:
        error_message = '\n'.join([f'{field}: {msg}' for field, msg in errores.items()])
        messagebox.showerror("Error de Validación", error_message)
        return
    datos_procesados = proceso_usuario(user_data)
    query = "INSERT INTO usuario (nombre, email) VALUES (%s, %s)"
    execute_query(query, (datos_procesados['nombre'], datos_procesados['email']))
    messagebox.showinfo("Éxito", "Usuario añadido correctamente.")


