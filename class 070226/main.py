from FechaAsistencia import *
def main():
    while True:
        print("\n Sistema de Asistencia")
        print("1. Agregar estudiante")
        print("2. Consultar estudiantes")
        print("3. Buscar estudiante por código")
        print("4. Salir")
        option = input("Elige una opción: ")

        if option == "1":
            codigo = int(input("Escribe el codigo del estudiante: "))
            nombre = input("Escribe el nombre del estudiante: ")
            apellido = input("Escribe el apellido del estudiante: ")
            estudiante_add(codigo, nombre, apellido)
        elif option == "2":
            Estudiante_lista()
        elif option == "3":
            codigo = input("Escribe el codigo del estudiante: ")
            estudiante =  search_lista(codigo)
            if estudiante:
                print(f'El estudiante {estudiante} existe')
            else:
                print(f'El estudiante {codigo} no existe')
        elif option == "4":
            print("Saliendo")
            break
        else:
            print("Opcion invalida")

if __name__ == '__main__':
    main()

