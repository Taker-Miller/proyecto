import tkinter as tk
from tkinter import messagebox, ttk
from register import create_register_gui
from logica import validar_usuario, registrar_incidencia, obtener_todas_las_incidencias, actualizar_incidencia, borrar_incidencia, registrar_asignacion, obtener_todas_las_asignaciones
from datetime import datetime

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión - Sistema de Mesa de Ayuda")
        self.root.geometry("400x250")
        self.root.configure(bg='#f0f0f0')
        self.user_id = None
        self.crear_interfaz_inicio_sesion()

    def crear_interfaz_inicio_sesion(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = tk.Frame(self.root, bg='#f0f0f0')
        frame.pack(padx=50, pady=50)

        tk.Label(frame, text="Nombre de usuario:", bg='#f0f0f0', font=('Arial', 12)).pack()
        self.username_entry = tk.Entry(frame, font=('Arial', 12), bd=2)
        self.username_entry.pack(pady=8)

        tk.Label(frame, text="Contraseña:", bg='#f0f0f0', font=('Arial', 12)).pack()
        self.password_entry = tk.Entry(frame, show="*", font=('Arial', 12), bd=2)
        self.password_entry.pack(pady=8)

        button_frame = tk.Frame(frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, expand=True)
        tk.Button(button_frame, text="Iniciar sesión", command=self.intentar_inicio_sesion, relief='raised', bd=3, font=('Arial', 12)).pack(side=tk.LEFT, expand=True)
        tk.Button(button_frame, text="Registrar", command=lambda: create_register_gui(self.root, self.crear_interfaz_inicio_sesion, self.crear_interfaz_inicio_sesion), relief='raised', bd=3, font=('Arial', 12)).pack(side=tk.RIGHT, expand=True)

    def intentar_inicio_sesion(self):
        nombre_usuario = self.username_entry.get()
        contrasena = self.password_entry.get()
        if not nombre_usuario or not contrasena:
            messagebox.showerror("Error de Inicio de Sesión", "El nombre de usuario y la contraseña no pueden estar vacíos.")
            return

        usuario = validar_usuario(nombre_usuario, contrasena)
        if usuario:
            self.user_id = usuario[0]
            self.crear_interfaz_principal()
        else:
            messagebox.showerror("Error de Inicio de Sesión", "Nombre de usuario o contraseña incorrectos.")

    def crear_interfaz_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Sistema de Mesa de Ayuda")
        self.root.geometry("1000x600")

        main_frame = tk.Frame(self.root, bg='#d0d0d0')
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, bg='#e0e0e0', width=200)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(left_frame, text="Registrar Incidencia", command=self.crear_interfaz_registrar_incidencia, font=('Arial', 12)).pack(pady=10)
        tk.Button(left_frame, text="Incidencias", command=self.crear_interfaz_lista_incidencias, font=('Arial', 12)).pack(pady=10)
        tk.Button(left_frame, text="Asignaciones", command=self.crear_interfaz_lista_asignaciones, font=('Arial', 12)).pack(pady=10)
        tk.Button(left_frame, text="Asignar", command=self.crear_interfaz_asignar_tecnico, font=('Arial', 12)).pack(pady=10)
        tk.Button(left_frame, text="Inventario", font=('Arial', 12)).pack(pady=10)
        tk.Button(left_frame, text="Clientes", font=('Arial', 12)).pack(pady=10)
        tk.Button(left_frame, text="Proveedores", font=('Arial', 12)).pack(pady=10)
        tk.Button(left_frame, text="Pedidos", font=('Arial', 12)).pack(pady=10)

        center_frame = tk.Frame(main_frame, bg='#ffffff')
        center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(center_frame, text="Bienvenido al Sistema de Mesa de Ayuda", font=('Helvetica', 16), bg='#ffffff').pack(pady=20)

    def crear_interfaz_registrar_incidencia(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Registrar Incidencia")
        self.root.geometry("600x400")

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Título:", font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.title_entry = tk.Entry(frame, font=('Arial', 12), width=40)
        self.title_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Descripción:", font=('Arial', 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.description_entry = tk.Entry(frame, font=('Arial', 12), width=40)
        self.description_entry.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Estado:", font=('Arial', 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.status_entry = tk.Entry(frame, font=('Arial', 12), width=40)
        self.status_entry.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Fecha de Creación:", font=('Arial', 12)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.creation_date_entry = tk.Entry(frame, font=('Arial', 12), width=40)
        self.creation_date_entry.grid(row=3, column=1, pady=5)

        tk.Label(frame, text="Fecha de Actualización:", font=('Arial', 12)).grid(row=4, column=0, sticky=tk.W, pady=5)
        self.update_date_entry = tk.Entry(frame, font=('Arial', 12), width=40)
        self.update_date_entry.grid(row=4, column=1, pady=5)

        tk.Button(frame, text="Guardar Incidencia", command=self.guardar_incidencia, font=('Arial', 12)).grid(row=5, columnspan=2, pady=10)
        tk.Button(frame, text="Regresar", command=self.crear_interfaz_principal, font=('Arial', 12)).grid(row=6, columnspan=2, pady=10)

    def guardar_incidencia(self):
        titulo = self.title_entry.get()
        descripcion = self.description_entry.get()
        estado = self.status_entry.get()
        fecha_creacion = self.creation_date_entry.get()
        fecha_actualizacion = self.update_date_entry.get()
        if registrar_incidencia(titulo, descripcion, estado, fecha_creacion, fecha_actualizacion, self.user_id):
            messagebox.showinfo("Registro de Incidencia", "Incidencia registrada exitosamente.")
            self.crear_interfaz_principal()
        else:
            messagebox.showerror("Error", "No se pudo registrar la incidencia.")

    def crear_interfaz_lista_incidencias(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Lista de Incidencias")
        self.root.geometry("800x600")

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        columnas = ("IDIncidencia", "Titulo", "Descripcion", "Estado", "FechaCreacion", "FechaActualizacion", "IDUsuario")
        self.tree = ttk.Treeview(frame, columns=columnas, show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER)

        self.cargar_incidencias()

        tk.Button(frame, text="Actualizar", command=self.actualizar_incidencia_gui, font=('Arial', 12)).pack(pady=10)
        tk.Button(frame, text="Borrar", command=self.borrar_incidencia, font=('Arial', 12)).pack(pady=10)
        tk.Button(frame, text="Regresar", command=self.crear_interfaz_principal, font=('Arial', 12)).pack(pady=10)

    def cargar_incidencias(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        incidencias = obtener_todas_las_incidencias()
        for incidencia in incidencias:
            self.tree.insert('', tk.END, values=incidencia)

    def actualizar_incidencia_gui(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione una incidencia para actualizar.")
            return

        incidencia = self.tree.item(selected_item)['values']

        ventana_actualizar = tk.Toplevel(self.root)
        ventana_actualizar.title("Actualizar Incidencia")
        ventana_actualizar.geometry("400x300")

        tk.Label(ventana_actualizar, text="Título:", font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        titulo_entry = tk.Entry(ventana_actualizar, font=('Arial', 12), width=30)
        titulo_entry.grid(row=0, column=1, pady=5)
        titulo_entry.insert(0, incidencia[1])

        tk.Label(ventana_actualizar, text="Descripción:", font=('Arial', 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        descripcion_entry = tk.Entry(ventana_actualizar, font=('Arial', 12), width=30)
        descripcion_entry.grid(row=1, column=1, pady=5)
        descripcion_entry.insert(0, incidencia[2])

        tk.Label(ventana_actualizar, text="Estado:", font=('Arial', 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        estado_entry = tk.Entry(ventana_actualizar, font=('Arial', 12), width=30)
        estado_entry.grid(row=2, column=1, pady=5)
        estado_entry.insert(0, incidencia[3])

        tk.Label(ventana_actualizar, text="Fecha de Actualización:", font=('Arial', 12)).grid(row=3, column=0, sticky=tk.W, pady=5)
        fecha_actualizacion_entry = tk.Entry(ventana_actualizar, font=('Arial', 12), width=30)
        fecha_actualizacion_entry.grid(row=3, column=1, pady=5)
        fecha_actualizacion_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        tk.Button(ventana_actualizar, text="Guardar Cambios", font=('Arial', 12), command=lambda: self.guardar_incidencia_actualizada(incidencia[0], titulo_entry.get(), descripcion_entry.get(), estado_entry.get(), fecha_actualizacion_entry.get(), ventana_actualizar)).grid(row=4, columnspan=2, pady=10)

    def guardar_incidencia_actualizada(self, id_incidencia, titulo, descripcion, estado, fecha_actualizacion, ventana):
        if actualizar_incidencia(id_incidencia, titulo, descripcion, estado, fecha_actualizacion):
            messagebox.showinfo("Actualizar Incidencia", "Incidencia actualizada exitosamente.")
            self.cargar_incidencias()
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se pudo actualizar la incidencia.")

    def borrar_incidencia(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione una incidencia para borrar.")
            return

        id_incidencia = self.tree.item(selected_item)['values'][0]
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea borrar esta incidencia?"):
            if borrar_incidencia(id_incidencia):
                messagebox.showinfo("Borrar Incidencia", "Incidencia borrada exitosamente.")
                self.cargar_incidencias()
            else:
                messagebox.showerror("Error", "No se pudo borrar la incidencia.")

    def crear_interfaz_lista_asignaciones(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Lista de Asignaciones")
        self.root.geometry("800x600")

        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        columnas = ("IDAsignacion", "IDIncidencia", "IDTecnico", "FechaAsignacion")
        self.assignment_tree = ttk.Treeview(frame, columns=columnas, show='headings')
        self.assignment_tree.pack(fill=tk.BOTH, expand=True)

        for col in columnas:
            self.assignment_tree.heading(col, text=col)
            self.assignment_tree.column(col, anchor=tk.CENTER)

        self.cargar_asignaciones()

        tk.Button(frame, text="Asignar Técnico", command=self.crear_interfaz_asignar_tecnico, font=('Arial', 12)).pack(pady=10)
        tk.Button(frame, text="Regresar", command=self.crear_interfaz_principal, font=('Arial', 12)).pack(pady=10)

    def cargar_asignaciones(self):
        for i in self.assignment_tree.get_children():
            self.assignment_tree.delete(i)
        asignaciones = obtener_todas_las_asignaciones()
        for asignacion in asignaciones:
            self.assignment_tree.insert('', tk.END, values=asignacion)

    def crear_interfaz_asignar_tecnico(self):
        ventana_asignar = tk.Toplevel(self.root)
        ventana_asignar.title("Asignar Técnico")
        ventana_asignar.geometry("400x300")

        tk.Label(ventana_asignar, text="ID Incidencia:", font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        id_incidencia_entry = tk.Entry(ventana_asignar, font=('Arial', 12), width=30)
        id_incidencia_entry.grid(row=0, column=1, pady=5)

        tk.Label(ventana_asignar, text="ID Técnico:", font=('Arial', 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        id_tecnico_entry = tk.Entry(ventana_asignar, font=('Arial', 12), width=30)
        id_tecnico_entry.grid(row=1, column=1, pady=5)

        tk.Label(ventana_asignar, text="Fecha de Asignación:", font=('Arial', 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        fecha_asignacion_entry = tk.Entry(ventana_asignar, font=('Arial', 12), width=30)
        fecha_asignacion_entry.grid(row=2, column=1, pady=5)
        fecha_asignacion_entry.insert(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        tk.Button(ventana_asignar, text="Asignar", font=('Arial', 12), command=lambda: self.guardar_asignacion(id_incidencia_entry.get(), id_tecnico_entry.get(), fecha_asignacion_entry.get(), ventana_asignar)).grid(row=3, columnspan=2, pady=10)

    def guardar_asignacion(self, id_incidencia, id_tecnico, fecha_asignacion, ventana):
        if registrar_asignacion(id_incidencia, id_tecnico, fecha_asignacion):
            messagebox.showinfo("Asignar Técnico", "Técnico asignado exitosamente.")
            self.cargar_asignaciones()
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se pudo asignar el técnico.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
