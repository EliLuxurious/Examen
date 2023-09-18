import tkinter as tk
from tkinter import ttk
from negocio_autor import AutorNegocio

class AutorInterfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Autores")
        self.root.geometry("400x400")

        self.negocio_autor = AutorNegocio()

        # Labels and Entry Fields
        self.nombre_label = ttk.Label(root, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(root)
        self.nombre_entry.pack()

        self.ap_paterno_label = ttk.Label(root, text="Apellido Paterno:")
        self.ap_paterno_label.pack()
        self.ap_paterno_entry = ttk.Entry(root)
        self.ap_paterno_entry.pack()

        self.ap_materno_label = ttk.Label(root, text="Apellido Materno:")
        self.ap_materno_label.pack()
        self.ap_materno_entry = ttk.Entry(root)
        self.ap_materno_entry.pack()

        self.codigo_label = ttk.Label(root, text="Código:")
        self.codigo_label.pack()
        self.codigo_entry = ttk.Entry(root)
        self.codigo_entry.pack()

        self.pais_label = ttk.Label(root, text="País:")
        self.pais_label.pack()
        self.pais_entry = ttk.Entry(root)
        self.pais_entry.pack()

        self.editorial_label = ttk.Label(root, text="Editorial:")
        self.editorial_label.pack()
        self.editorial_entry = ttk.Entry(root)
        self.editorial_entry.pack()

        # Buttons
        self.registrar_button = ttk.Button(root, text="Registrar Autor", command=self.registrar_autor)
        self.registrar_button.pack()

        self.editar_button = ttk.Button(root, text="Editar Autor", command=self.editar_autor)
        self.editar_button.pack()

        self.listar_button = ttk.Button(root, text="Listar Autores", command=self.listar_autores)
        self.listar_button.pack()

        self.salir_button = ttk.Button(root, text="Salir", command=root.quit)
        self.salir_button.pack()

    def registrar_autor(self):
        nombre = self.nombre_entry.get()
        ap_paterno = self.ap_paterno_entry.get()
        ap_materno = self.ap_materno_entry.get()
        codigo = self.codigo_entry.get()
        pais = self.pais_entry.get()
        editorial = self.editorial_entry.get()

        self.negocio_autor.registrar_autores(nombre, ap_paterno, ap_materno, codigo, pais, editorial)
        resultado = self.negocio_autor.guardar_autores()
        print(resultado)

    def editar_autor(self):
        # Agrega aquí la lógica para editar un autor
        pass

    def listar_autores(self):
        # Agrega aquí la lógica para listar los autores
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = AutorInterfaz(root)
    root.mainloop()


