class Estudiante:
    def __init__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'{self.codigo} {self.nombre} {self.apellido}'

