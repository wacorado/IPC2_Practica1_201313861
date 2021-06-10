from NodoContacto import Contacto

class ListaContactos:
    def __init__(self):
        self.primero = None
        #self.ultimo = None

    def AgregarAlFinalOrdenado(self, nombre, apellido, numero):
        nuevo = Contacto(nombre, apellido, numero)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            if(tmp.numero==nuevo.numero):
                print("\n########-------Contacto ya Registrado----------------###########\n")
            else:
                while tmp.siguiente is not None:
                    tmp = tmp.siguiente
                tmp.siguiente = nuevo
                nuevo.anterior = tmp
    
    def AgregarAlInicio(self, nombre, apellido, numero):
        if self.primero is None:
            nuevo = Contacto(nombre, apellido, numero)
            self.primero = nuevo
            print("Contacto Ingresado al Inicio")
            return
        nuevo = Contacto(nombre, apellido, numero)
        nuevo.anterior = self.primero
        self.primero.siguiente = nuevo
        self.primero = nuevo

    def imprimirAgenda(self):
        temporal = self.primero
        while temporal != None:
                print("Nombre Contacto: " + temporal.nombre+"\nApellido: "+ temporal.apellido+"\n Numero Telefonico: "+temporal.numero)
                temporal = temporal.siguiente
                print("-----------------------------------------------------------------------------------------------\n")

    def ingresoOrdenado(self, nombre, apellido, numero):
         
        nuevo = Contacto(nombre,apellido,numero)
 
        # Verificamos si la Lista esta Vacia
        if self.primero is None:
            self.primero = nuevo

        elif(self.primero.numero==nuevo.numero):
                print("\n########-------Contacto ya Registrado----------------###########\n")
        
        elif self.primero.apellido.upper()> nuevo.apellido.upper():
            nuevo.siguiente = self.primero
            nuevo.siguiente.anterior = nuevo
            self.primero = nuevo
        elif self.primero.apellido.upper()== nuevo.apellido.upper():
            
            if self.primero.nombre.upper()> nuevo.nombre.upper():
                nuevo.siguiente = self.primero
                nuevo.siguiente.anterior = nuevo
                self.primero = nuevo
            else:
                auxiliar = self.primero
                while ((auxiliar.siguiente is not None) and (auxiliar.siguiente.nombre.upper() < nuevo.nombre.upper())):
                    auxiliar = auxiliar.siguiente
    
                    nuevo.siguiente = auxiliar.siguiente

                    if auxiliar.siguiente is not None:
                        nuevo.siguiente.anterior = nuevo
 
                    auxiliar.siguiente = nuevo
                    nuevo.anterior = auxiliar
            
        else:
            auxiliar = self.primero
            # Locate the node after which
            # the new node  is to be inserted
            while ((auxiliar.siguiente is not None) and
                   (auxiliar.siguiente.apellido.upper() < nuevo.apellido.upper())):
                auxiliar = auxiliar.siguiente
     
            # Make the appropriate links
            nuevo.siguiente = auxiliar.siguiente
 
            # If the new node is not inserted
            # at the end of the list
            if auxiliar.siguiente is not None:
                nuevo.siguiente.anterior = nuevo
 
            auxiliar.siguiente = nuevo
            nuevo.anterior = auxiliar