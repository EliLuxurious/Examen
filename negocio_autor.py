import pandas as pd
from Autor import Autor

class AutorNegocio():
    
    listado_autores = []
    registro_autores = 'C:/Users/Elia/Desktop/PROGRAMACION/Python/CICLO 3/Educativa/listado_autor/listado_autor.xlsx'

    def __init__(self):
        self.listado_autores = []

    def obtener_autores(self):
        df = pd.read_excel(self.registro_autores)
        listado_autores = []
        for index, row in df.iterrows():
            autor = Autor(row['Nombre'], row['Apellido_Paterno'], row['Apellido_Materno'], row['Fecha_Nacimiento'], row['Cod_Autor'], row['Pais'], row['Editorial'])
            listado_autores.append(autor)
        return listado_autores


    def registrar_autores(self,nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial):
        self.listado_autores = self.obtener_autores()
        autor = Autor(nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial)
        self.listado_autores.append(autor)
        print(f'Se agregó un autor: {len(self.listado_autores)}')

    def guardar_autores(self):
        if len(self.listado_autores) > 0:
            data = []
            for autor in self.listado_autores:
                data.append([autor.nombre, autor.ap_paterno, autor.ap_materno, autor.fecha_nacimiento, autor.cod_autor, autor.pais, autor.editorial])
            columnas = ['Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Fecha_Nacimiento', 'Cod_Autor', 'Pais', 'Editorial']
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registro_autores, index=False, engine='openpyxl')
            return f'Se registraron correctamente los datos de los autores'
        else:
            return f'Se generó un error al registrar a los autores'


    def editar_autores(self, indice, nombre, ap_paterno, ap_materno, fecha_nacimiento, codigo, pais, editorial):
        df = pd.read_excel(self.registro_autores)
        df.loc[indice, 'Nombre'] = nombre
        df.loc[indice, 'Apellido_Paterno'] = ap_paterno
        df.loc[indice, 'Apellido_Materno'] = ap_materno
        df.loc[indice, 'Fecha_Nacimiento'] = fecha_nacimiento
        df.loc[indice, 'Codigo'] = codigo
        df.loc[indice, 'Pais'] = pais
        df.loc[indice, 'Editorial'] = editorial
        df.to_excel(self.registro_autores, index=False, engine='openpyxl')
        return f'Actualización correcta'

    def buscar_autor_por_codigo(self, codigo):
        for autor in self.listado_autores:
            if autor.cod_autor == codigo:
                return autor
        return None
