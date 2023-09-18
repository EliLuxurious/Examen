from negocio_autor import AutorNegocio
import pandas as pd
from openpyxl import Workbook

negocio_autor = AutorNegocio()

def registrar_autores():
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    fecha_nacimiento = input('Ingrese fecha_nacimiento: ')
    cod_autor = input('Ingrese cod_autor: ')
    pais = input('Ingrese pais: ')
    editorial = input('Ingrese editorial: ')
    negocio_autor.registrar_autores(nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial)
    negocio_autor.guardar_autores()
    print(f'Registro exitoso del autor')

def obtener_autores():
    listado_autores = negocio_autor.obtener_autores()
    for autor in listado_autores:
        print(autor.imprimir())

def editar_autores():
    indice = int(input('Ingrese el índice del autor a editar: '))
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    fecha_nacimiento = input('Ingrese fecha_nacimiento: ')
    cod_autor = input('Ingrese cod_autor: ')
    pais = input('Ingrese pais: ')
    editorial = input('Ingrese editorial: ')
    print(negocio_autor.editar_autores(indice, nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial ))

opciones = {
    "1": registrar_autores,
    "2": obtener_autores,
    "3": editar_autores,
    "4": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar autores")
    print("2. Listar autores")
    print("3. Editar autores")
    print("4. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")