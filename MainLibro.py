from Categoria import Categoria  # Asumiendo que tienes una clase Categoria
from negocio_autor import AutorNegocio
from negocio_libro import NegocioLibro
from negocio_categoria import NegocioCategoria  # Agregar importación para la clase NegocioCategoria

negocio_autor = AutorNegocio()
negocio_libro = NegocioLibro()
negocio_categoria = NegocioCategoria()  # Crear una instancia de NegocioCategoria

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
    print(negocio_autor.editar_autores(indice, nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial))

def registrar_libros():
    codigo_libro = input('Ingrese código del libro: ')
    titulo = input('Ingrese título del libro: ')
    year = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')
    autor = input('Ingrese el autor del libro (Código del autor): ')
    
    # Obtener el autor del registro de autores (asumiendo que está implementado)
    autor_encontrado = negocio_autor.buscar_autor_por_codigo(autor)
    if autor_encontrado:
        negocio_libro.registrar_libro(codigo_libro, titulo, year, tomo, autor_encontrado)
        resultado = negocio_libro.guardar_libros()
        print(resultado)
    else:
        print("El autor no existe. Registre al autor antes de agregar el libro.")

def obtener_libros():
    listado_libros = negocio_libro.obtener_libros()
    for libro in listado_libros:
        autor = libro.mostrar_autor()
        autor_info = f"Autor: {autor.nombre} {autor.ap_paterno} {autor.ap_materno}" if autor else "Autor no asignado"
        print(f"Código del libro: {libro.get_codigo_libro()}\nTítulo: {libro.get_titulo()}\nAño: {libro.get_year()}\nTomo: {libro.get_tomo()}\n{autor_info}\n")

def editar_libros():
    indice = int(input('Ingrese el índice del libro a editar: '))
    codigo_libro = input('Ingrese código del libro: ')
    titulo = input('Ingrese título del libro: ')
    year = input('Ingrese año del libro: ')
    tomo = input('Ingrese tomo del libro: ')
    autor = input('Ingrese el autor del libro (Código del autor): ')
    
    # Obtener el autor del registro de autores (asumiendo que está implementado)
    autor_encontrado = negocio_autor.buscar_autor_por_codigo(autor)
    if autor_encontrado:
        print(negocio_libro.editar_libro(indice, codigo_libro, titulo, year, tomo, autor_encontrado))
    else:
        print("El autor no existe. Registre al autor antes de editar el libro.")

def asignar_libro_a_categoria():
    codigo_libro = input('Ingrese código del libro: ')
    categoria_codigo = input('Ingrese código de la categoría: ')
    
    libro = negocio_libro.buscar_libro_por_codigo(codigo_libro)
    categoria = negocio_categoria.buscar_categoria_por_codigo(categoria_codigo)
    
    if libro and categoria:
        libro.asignar_categoria(categoria)
        resultado = negocio_libro.guardar_libros()
        print(f'Libro asignado a la categoría "{categoria.get_categoria()}".')
    else:
        print("El libro o la categoría no existen.")

def registrar_categoria():
    cod_categoria = input('Ingrese el código de la categoría: ')
    categoria = input('Ingrese el nombre de la categoría: ')
    negocio_categoria.registrar_categoria(cod_categoria, categoria)
    print(f'Categoría "{categoria}" registrada con éxito.')

def editar_categoria():
    cod_categoria = input('Ingrese el código de la categoría que desea editar: ')
    nueva_categoria = input('Ingrese el nuevo nombre de la categoría: ')
    negocio_categoria.editar_categoria(cod_categoria, nueva_categoria)
    print(f'Categoría con código "{cod_categoria}" editada con éxito.')

def listar_categorias():
    categorias = negocio_categoria.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas.")
    else:
        print("Lista de Categorías:")
        for categoria in categorias:
            print(f"Código de Categoría: {categoria.get_cod_categoria()}, Nombre: {categoria.get_categoria()}")

opciones = {
    "1": registrar_autores,
    "2": obtener_autores,
    "3": editar_autores,
    "4": registrar_libros,
    "5": obtener_libros,
    "6": editar_libros,
    "7": asignar_libro_a_categoria,
    "8": registrar_categoria,     
    "9": editar_categoria,      
    "10": listar_categorias,  
    "11": exit
}

while True:
    print("##########################")
    print("Menú:")
    print("1. Registrar autores")
    print("2. Listar autores")
    print("3. Editar autores")
    print("4. Registrar libros")
    print("5. Listar libros")
    print("6. Editar libros")
    print("7. Asignar libro a categoría")
    print("8. Registrar Categoría")   
    print("9. Editar Categoría")       
    print("10. Listar Categorías")     
    print("11. Salir")
    print("##########################")
    
    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")