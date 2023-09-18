from Categoria import Categoria

class NegocioCategoria():
    lista_categorias = []

    def __init__(self):
        self.lista_categorias = []

    def obtener_categorias(self):
        return self.lista_categorias

    def registrar_categoria(self, cod_categoria, categoria):
        categoria_existente = self.buscar_categoria_por_codigo(cod_categoria)
        if categoria_existente:
            print("La categoría ya existe.")
        else:
            nueva_categoria = Categoria(cod_categoria, categoria)
            self.lista_categorias.append(nueva_categoria)
            print("Categoría registrada con éxito.")

    def editar_categoria(self, cod_categoria, nueva_categoria):
        categoria_existente = self.buscar_categoria_por_codigo(cod_categoria)
        if categoria_existente:
            categoria_existente.set_categoria(nueva_categoria)
            print("Categoría editada con éxito.")
        else:
            print("La categoría no existe.")

    def buscar_categoria_por_codigo(self, cod_categoria):
        for categoria in self.lista_categorias:
            if categoria.get_cod_categoria() == cod_categoria:
                return categoria
        return None
