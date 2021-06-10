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
    print()
    Agenda.ingresoOrdenado(nombreC,apellidoC,numeroC)
    Agenda.imprimirAgenda()

def buscarContacto():
    numero = input("Ingrese el Numero a Buscar: \n")
    if(Agenda.Buscar(numero) != True):
        opcion=input("Desea Registrar Contacto: Si/No \n")
        if(opcion.upper()=="SI"):
            agregarContacto()
        elif(opcion.upper()=="NO"):
            menu()

def generarGrafica():
    Agenda.generarGrafico()

ciclo=True
while(ciclo):
    numero = menu()
    if numero == "1":
        print("Opcion1")
        agregarContacto()
        input("")
    elif numero == "2":
        print("Opcion2")
        buscarContacto()
        input("")
    elif numero == "3":
        print("Opcion3")
        generarGrafica()
        input("")
    elif numero == "4":
        #salir()
        input("")
        ciclo=False
    elif numero >= str(5):
        print("Opcion no Valida debe ingresar una opcion entre 1 y 4")
        input("")

