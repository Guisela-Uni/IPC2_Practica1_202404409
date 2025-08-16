import os
#Menú inicial
def menu1():
    print("--------------- BIENVENIDO A LA BIBLIOTECA  ---------------")
    print("Aqui puedes gestionar el prestamo de tus libros, porfavor, selecciona una opción: ")
    print("1. Registrar libro")
    print("2. Gestionar materiales")
    print("3. Salir")

def menu2():
    print("--------------- REGISTRO DE LIBROS ---------------")
    print("Selecciona que tipo de material bibliotecario quieres registrar")
    print("1. Libro fisico")
    print("2. Libro digital")
    print("3. Regresar al menu")

def menu3():
    print("--------------- Gestion de materiales ---------------")
    print("Selecciona que tipo operación desesas realizar con los libros del sistema: ")
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Consultar información de libros")
    print("Regresar al menu")

def registro():
    while True:
        menu2()
        opcion1=input("opcion elegida: ")
        if opcion1 =="1":
            regFisico() #funcion para registrar libro fisico

        elif opcion1 == "2":
            regVirtual() #Funcion para registrar libro virtual

        elif opcion1 == "3":
            print("Regresando a menu")
            break
        
        else:
            print("Haz presionado una opcion incorrecta,")

def gestion():
    while True:
        menu3()
        opcion3=input("opcion elegida: ")
        if opcion3 =="1":
            prestar() #funcion para prestar libro 

        elif opcion3 == "2":
            devolver() #Funcion para devolver libro 

        elif opcion3 == "3":
            infoLibro() #Funcion para ver informacion del libro 

        elif opcion3 == "4":
            print("Regresando a menu")
            break
        
        else:
            print("Haz presionado una opcion incorrecta,")


while True:
    os.system('cls')
    menu1()
    opcion = input("Opcion elegida: ")

    if opcion == "1":
        os.system('cls') #limpia la consola
        registro()

    elif opcion == "2":
        print("Ha seleccionado la opción 2")
        os.system('cls') 
        gestion()

    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Haz seleccionado una opcion invalida.")

