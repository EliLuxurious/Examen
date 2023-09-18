from Persona import Persona

class Autor(Persona):
    cod_autor = ''
    pais = ''
    editorial = ''
    
    #Definimos el constructor
    def __init__(self, nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial):
        super().__init__(nombre, ap_paterno, ap_materno, fecha_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

    def get_cod_autor(self):
        return self.cod_autor
    
    def set_cod_autor(self, cod_autor):
        self.cod_autor = cod_autor
    
    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais

    def get_editorial(self):
        return self.editorial

    def set_editorial(self, editorial):
        self.editorial = editorial

    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.cod_autor
        pais = self.pais
        editorial = self.editorial
        return f'Datos del docente es : {per_data}, Codigo: {codigo} Pais: {pais}, Editorial: {editorial}'