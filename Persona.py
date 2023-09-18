class Persona:
    nombre = ""
    ap_paterno = ""
    ap_materno = ""
    fecha_nacimiento = ""

    # constructor
    def __init__(self, nombre, ap_paterno, ap_materno, fecha_nacimiento):
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.fecha_nacimiento = fecha_nacimiento


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_ap_paterno(self):
        return self.ap_paterno

    def set_ap_paterno(self, ap_paterno):
        self.ap_paterno = ap_paterno

    def get_ap_materno(self):
        return self.ap_materno

    def set_ap_materno(self, ap_materno):
        self.ap_materno = ap_materno

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def imprimir(self):
        Nombres = self.nombre
        Apellidos = self.ap_paterno + ' ' + self.ap_materno
        return f' {Nombres =},  {Apellidos =}'