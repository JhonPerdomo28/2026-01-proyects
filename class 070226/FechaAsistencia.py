from Estudiantes import Estudiante

lista_estudiantes = []
lista_asistencia = {}

def estudiante_add(codigo, nombre, apellido):
    estudiante = Estudiante(codigo, nombre, apellido)
    lista_estudiantes.append(estudiante)
    lista_asistencia[codigo] = {
        "estudiante": estudiante,
        "asistencias": []
    }
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
def search_attendance_list(codigo):
    if codigo not in lista_asistencia:
        print("Estudiante no inscritos.")
        return

    estudiante = lista_asistencia[codigo]["estudiante"]
    asistencias = lista_asistencia[codigo]["asistencias"]

    print(f"\nAsistencia de {estudiante.nombre} {estudiante.apellido}:")

    if not asistencias:
        print("No hay asistencias registradas.\n")
        return

    total = len(asistencias)

    print(f"{estudiante.nombre} {estudiante.apellido} asistió a {total} clases.")


def attendance_list(codigo):
    if codigo in lista_asistencia:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        presente_input = input("¿Está presente? (s/n): ")

        presente = presente_input.lower() == "s"

        lista_asistencia[codigo]["asistencias"].append({
            "fecha": fecha,
            "presente": presente
        })
        print(f"fecha asistencia: {fecha} para estudiante: {codigo} registrada.")
        return
    else:
        print("Estudiante no encontrado.")
        return


