from Estudiantes import Estudiante

lista_estudiantes = []
lista_asistencia = []

def estudiante_add(codigo, nombre, apellido):
    estudiante = Estudiante(codigo, nombre, apellido)
    lista_estudiantes.append(estudiante)
    print(f"Estudiante añadido: {estudiante} ")

def Estudiante_lista():
    if not lista_estudiantes:
        print("No hay estudiantes inscritos.")
        return
    else:
        print("Estudiantes inscritos:")
        for estudiante in lista_estudiantes:
            print(estudiante)

def search_lista(codigo):
    for estudiante in lista_estudiantes:
        if estudiante.codigo == codigo:
            return estudiante
        else:
            print("El estudiante no existe.")
            return None

#def attendance_list():




