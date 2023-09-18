from negocio_autor import AutorNegocio
from negocio_libro import NegocioLibro
from negocio_categoria import NegocioCategoria

negocio_autor = AutorNegocio()
negocio_libro = NegocioLibro()
negocio_categoria = NegocioCategoria()

def registrar_autor():
    nombre = input('Ingrese nombre del autor: ')
    ap_paterno = input('Ingrese apellido paterno del autor: ')
    ap_materno = input('Ingrese apellido materno del autor: ')
    fecha_nacimiento = input('Ingrese fecha de nacimiento del autor: ')
    cod_autor = input('Ingrese código del autor: ')
    pais = input('Ingrese país del autor: ')
    editorial = input('Ingrese editorial del autor: ')
    negocio_autor.registrar_autor(nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial)
    negocio_autor.guardar_autores()
    print(f'Registro exitoso del autor')

def obtener_autores():
    listado_autores = negocio_autor.obtener_autores()
    for autor in listado_autores:
        print(autor.imprimir())

def editar_autor():
    indice = int(input('Ingrese el índice del autor a editar: '))
    nombre = input('Ingrese nombre del autor: ')
    ap_paterno = input('Ingrese apellido paterno del autor: ')
    ap_materno = input('Ingrese apellido materno del autor: ')
    fecha_nacimiento = input('Ingrese fecha de nacimiento del autor: ')
    cod_autor = input('Ingrese código del autor: ')
    pais = input('Ingrese país del autor: ')
    editorial = input('Ingrese editorial del autor: ')
    print(negocio_autor.editar_autor(indice, nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial))

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

def registrar_libro():
    codigo_libro = input('Ingrese código del libro: ')
    titulo = input('Ingrese título del libro: ')
    year = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')
    autor = input('Ingrese el código del autor del libro: ')
    categoria = input('Ingrese el código de la categoría del libro: ')

    autor_encontrado = negocio_autor.buscar_autor_por_codigo(autor)
    if autor_encontrado:
        negocio_libro.registrar_libro(codigo_libro, titulo, year, tomo, autor_encontrado)
        resultado = negocio_libro.guardar_libros()
        print(resultado)
    else:
        print("El autor no existe. Registre al autor antes de agregar el libro.")

    categoria_encontrada = negocio_categoria.buscar_categoria_por_codigo(categoria)
    if categoria_encontrada:
        categoria_encontrada.asignar_libro(codigo_libro)
        resultado_categoria = negocio_categoria.guardar_categorias()
        print(resultado_categoria)
    else:
        print("La categoría no existe. Registre la categoría antes de asignar el libro.")

def obtener_libros():
    listado_libros = negocio_libro.obtener_libros()
    for libro in listado_libros:
        autor = libro.mostrar_autor()
        autor_info = f"Autor: {autor.nombre} {autor.ap_paterno} {autor.ap_materno}" if autor else "Autor no asignado"
        print(f"Código del libro: {libro.get_codigo_libro()}\nTítulo: {libro.get_titulo()}\nAño: {libro.get_year()}\nTomo: {libro.get_tomo()}\n{autor_info}\n")

def editar_libro():
    indice = int(input('Ingrese el índice del libro a editar: '))
    codigo_libro = input('Ingrese código del libro: ')
    titulo = input('Ingrese título del libro: ')
    year = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')
    autor = input('Ingrese el código del autor del libro: ')

    autor_encontrado = negocio_autor.buscar_autor_por_codigo(autor)
    if autor_encontrado:
        print(negocio_libro.editar_libro(indice, codigo_libro, titulo, year, tomo, autor_encontrado))
    else:
        print("El autor no existe. Registre al autor antes de editar el libro.")

opciones = {
    "1": registrar_autor,
    "2": obtener_autores,
    "3": editar_autor,
    "4": registrar_categoria,
    "5": editar_categoria,
    "6": listar_categorias,
    "7": registrar_libro,
    "8": obtener_libros,
    "9": editar_libro,
    "10": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar Autor")
    print("2. Listar Autores")
    print("3. Editar Autor")
    print("4. Registrar Categoría")
    print("5. Editar Categoría")
    print("6. Listar Categorías")
    print("7. Registrar Libro")
    print("8. Listar Libros")
    print("9. Editar Libro")
    print("10. Salir")
    print("##########################")

    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
