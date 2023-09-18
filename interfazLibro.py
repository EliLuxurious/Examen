import tkinter as tk
from tkinter import ttk
from negocio_libro import NegocioLibro

root = tk.Tk()
root.title("Registro de Libro")
root.geometry("400x550")

negocio = NegocioLibro()

status_label = ttk.Label(root, text="")
status_label.config(text=f"Registro en el índice {1} editado y guardado.")

def limpiar_controles():
    codigo_libro_entry.delete(0, tk.END)
    titulo_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    tomo_entry.delete(0, tk.END)

def guardar_libros():
    codigo_libro = codigo_libro_entry.get()
    titulo = titulo_entry.get()
    year = year_entry.get()
    tomo = tomo_entry.get()
    
    negocio.registrar_libro(codigo_libro, titulo, year, tomo)
    resultado = negocio.guardar_libros()
    status_label.config(text=resultado)
    limpiar_controles()

def salir():
    root.quit()

# Labels and Entry Fields
codigo_libro_label = ttk.Label(root, text="Código libro:")
codigo_libro_label.pack()
codigo_libro_entry = ttk.Entry(root)
codigo_libro_entry.pack()

titulo_label = ttk.Label(root, text="Título:")
titulo_label.pack()
titulo_entry = ttk.Entry(root)
titulo_entry.pack()

year_label = ttk.Label(root, text="Año:")
year_label.pack()
year_entry = ttk.Entry(root)
year_entry.pack()

tomo_label = ttk.Label(root, text="Tomo:")
tomo_label.pack()
tomo_entry = ttk.Entry(root)
tomo_entry.pack()

guardar_button = ttk.Button(root, text="Guardar", command=guardar_libros)
guardar_button.pack()

salir_button = ttk.Button(root, text="Cancelar", command=salir)
salir_button.pack()

status_label.pack()

root.mainloop()
