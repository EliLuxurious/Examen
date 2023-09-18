from negocio_categoria import CategoriaNegocio

negocio_categoria = CategoriaNegocio()

def registrar_categoria():
    cod_categoria = input('Ingrese el código de la categoría: ')
    categoria = input('Ingrese el nombre de la categoría: ')
    negocio_categoria.registrar_categoria(cod_categoria, categoria)

def editar_categoria():
    cod_categoria = input('Ingrese el código de la categoría que desea editar: ')
    nueva_categoria = input('Ingrese el nuevo nombre de la categoría: ')
    negocio_categoria.editar_categoria(cod_categoria, nueva_categoria)

def listar_categorias():
    categorias = negocio_categoria.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas.")
    else:
        print("Lista de Categorías:")
        for categoria in categorias:
            print(f"Código de Categoría: {categoria.get_cod_categoria()}, Nombre: {categoria.get_categoria()}")

opciones = {
    "1": registrar_categoria,
    "2": editar_categoria,
    "3": listar_categorias,
    "4": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar Categoría")
    print("2. Editar Categoría")
    print("3. Listar Categorías")
    print("4. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
