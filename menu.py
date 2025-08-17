from clases.libroDigital import libroDigital
from clases.libroFisico import libroFisico
from clases.mastermind import mastermind
import os
import time

mind = mastermind() #definiendo mastermind
#Menú inicial
def menu1():
    print("------------------- BIENVENIDO A LA BIBLIOTECA  -------------------")
    print("Aqui puedes gestionar el prestamo de tus libros, porfavor, selecciona una opción: ")
    print("1. Registrar libro")
    print("2. Gestionar materiales")
    print("3. Salir")

#Registrar libro
def registrarLibro():
    print("-------------------  REGISTRAR LIBRO -------------------")
    print("| 1. Registrar libro fisico                             |")
    print("| 2. Registrar libro virtual                            |")
    print("| 3. Regresar al menu                                   |")
    print("|-------------------------------------------------------|")
    opcion = int(input("ingresa tu opcion: "))
    match opcion:
        case 1:
            agregarLibroFisico()
        case 2:
            agregarLibroDigital()
        case 3:
            print("Volviendo al menu principal")
            time.sleep(1)
            print("")

def agregarLibroDigital():
    print("---------------- REGISTRAR LIBRO DIGITAL ----------------")
    print("|Escriba los datos que se solicitan:                     |")
    print("| Titulo del libro                                       |")
    titulo = input()
    print("| Autor del libro                                        |")
    autor = input()
    print("| Codigo único:                                          |")
    codigo = int(input())
    print("| Tamaño del arhivo                                      |")
    pesoArchivo = int(input())

    nuevoLibroDigital = libroDigital(titulo, autor, codigo, pesoArchivo)
    mind.nuevoLibro(nuevoLibroDigital)
    print("<<<  Libro digital creado exitosamente  >>>")
    time.sleep(1)
    print("")

def agregarLibroFisico():
    print("---------------- REGISTRAR LIBRO FISICO ----------------")
    print("|Escriba los datos que se solicitan:                     |")
    print("| Titulo del libro                                       |")
    titulo = input()
    print("| Autor del libro                                        |")
    autor = input()
    print("| Codigo único:                                          |")
    codigo = int(input())
    print("| Número de ejemplar                                      |")
    ejemplar = int(input())

    nuevoLibroFisico = libroFisico(titulo, autor, codigo, ejemplar)
    mind.nuevoLibro(nuevoLibroFisico)
    print("<<<  Libro fisico creado exitosamente  >>>")
    time.sleep(1)
    print("")



while True:
    os.system('cls')
    menu1()
    opcion = input("Opcion elegida: ")

    if opcion == "1":
        os.system('cls') #limpia la consola
        registrarLibro()

    elif opcion == "2":
        print("Ha seleccionado la opción 2")
        os.system('cls') 
        

    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Haz seleccionado una opcion invalida.")

