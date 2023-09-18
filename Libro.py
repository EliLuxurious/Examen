from Autor import Autor

class Libro(Autor):
    codigo_libro = ''
    titulo = ''
    year = ''
    tomo = ''

    def __init__(self, codigo_libro, titulo, year, tomo):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.year = year
        self.tomo = tomo
        self.autor = None  # Atributo para almacenar al autor asignado

    def set_codigo_libro(self, codigo_libro):
        self.codigo_libro = codigo_libro

    def get_codigo_libro(self):
        return self.codigo_libro

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year
    
    def set_tomo(self, tomo):
        self.tomo = tomo
    
    def get_tomo(self):
        return self.tomo
    
    def asignar_autor(self, autor):
        self.autor = autor
    
    def mostrar_autor(self):
        return self.autor
    
    def reporte(self):
        return f"Reporte del curso {self.titulo}\nCodigo del libro: {self.get_codigo_libro}\nAño: {self.year}\nTomo: {self.tomo}"