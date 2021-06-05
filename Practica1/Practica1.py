from ListaContactos import ListaContactos

Agenda=ListaContactos()

def menu():
    print("1. Ingresar Contacto")
    print("2. Buscar Contacto")
    print("3. Visualizar Agenda")
    print("4. Salir")
    opcion = input("Ingrese una opccion: \n")
    return opcion

def agregarContacto():
    nombreC=input("Ingrese el Nombre del Contacto:\n")
    apellidoC=input("Ingrse el Apellido del Contacto: \n")
    numeroC=input("Ingrese el numero del Contacto: \n")
    Agenda.AgregarAlFinal(nombreC,apellidoC,numeroC)
    Agenda.imprimirAgenda()


ciclo=True
while(ciclo):
    numero = menu()
    if numero == "1":
        print("Opcion1")
        agregarContacto()
        input("")
    elif numero == "2":
        print("Opcion2")
        input("")
    elif numero == "3":
        print("Opcion3")
        input("")
    elif numero == "4":
        #salir()
        input("")
        ciclo=False
    elif numero >= str(5):
        print("Opcion no Valida debe ingresar una opcion entre 1 y 4")
        input("")

