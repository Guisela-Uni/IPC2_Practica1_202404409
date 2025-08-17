from clases.libroDigital import libroDigital
from clases.libroFisico import libroFisico
from clases.mastermind import mastermind
from clases.materialBiblioteca import materialBiblioteca
import os
import time
import datetime

mind = mastermind() #definiendo mastermind
fecha_actual = datetime.date.today().strftime("%d/%m/%Y")

def fechaSieteDias():
    fecha_actual = datetime.date.today()
    fecha_futura = fecha_actual + datetime.timedelta(days=7)
    return fecha_futura.strftime("%d/%m/%Y")

def fechaTresDias():
    fecha_actual = datetime.date.today()
    fecha_futura = fecha_actual + datetime.timedelta(days=3)
    return fecha_futura.strftime("%d/%m/%Y")

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

#Gestionar materiales
def gestionarLibros():
    print("-------------------   GESTIONAR LIBROS  --------------------")
    print("| 1. Prestar libro                                           |")
    print("| 2. Devolver libro                                          |")
    print("| 3. Consultar información                                   |")
    print("| 4. Regresar al menu                                        |")
    print("|------------------------------------------------------------|")
    opcion = int(input("ingresa tu opcion: "))
    match opcion:
        case 1:
            prestarLibro()
        case 2:
            devolverLibro()
        case 3:
            consultarInformacion()
        case 4:
            print("Volviendo al menu principal")
            time.sleep(1)
            print("")

def prestarLibro():
    print("-------------------- PRESTAR LIBRO --------------------")
    print("|Escriba los datos que se solicitan:                   |")
    print("| Codigo del libro                                     |")
    codigo = int(input())
    print("| Nombre del usuario                                   |")
    usuario = input()
    print("<<< Fecha de prestamo: ", fecha_actual," >>>") 
    libroDigital.prestarLibro(codigo, usuario)
    print("Libro devuelto exitosamente, debe ser devuelto en fecha ", fechaSieteDias())
    time.sleep(1)
    print("")

def devolverLibro():
    print("-------------------- DEVOLVER LIBRO --------------------")
    print("|Escriba los datos que se solicitan:                     |")
    print("| Codigo del libro                                       |")
    codigo = int(input())
    print("| Nombre del usuario                                     |")
    usuario = input()
    print("Libro devuelto exitosamente en fecha ", fecha_actual)
    libroDigital.devolverLibro(codigo, usuario)
    time.sleep(1)
    print("")

def consultarInformacion():
    print("---------------- CONSULTAR INFORMACION ----------------")
    print("|Escriba los datos que se solicitan:                     |")
    print("| Codigo del libro                                         |")
    codigo = int(input())
    materialBiblioteca.mostrarInfo()
    time.sleep(1)
    print("")




# Bucle principal del menú
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
        gestionarLibros()

    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Haz seleccionado una opcion invalida.")

