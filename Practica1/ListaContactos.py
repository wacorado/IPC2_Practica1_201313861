from NodoContacto import Contacto
import os

def crearNodo(identificador,nombre, shape):
    return identificador + "[label=\""+ nombre + "\",shape="+ shape + "]\n"

def unionNodo(nodoA,nodoB):
    return nodoA + "->" + nodoB +"\n"
    
class ListaContactos:
    def __init__(self):
        self.primero = None
        #self.ultimo = None
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
        #Verificamos  que el numero no este registrado
        elif(self.primero.numero==nuevo.numero):
                print("\n########-------Contacto ya Registrado----------------###########\n")
        #verificamos que sea menor que nodio anterior para guardar detras de el
        elif self.primero.apellido.upper()> nuevo.apellido.upper():
            nuevo.siguiente = self.primero
            nuevo.siguiente.anterior = nuevo
            self.primero = nuevo
        #Verificar cuando el apellido es igual 
        elif self.primero.apellido.upper()== nuevo.apellido.upper():
            #ordenamos por nombre si primero es menor guarda detras de el 
            if self.primero.nombre.upper()> nuevo.nombre.upper():
                nuevo.siguiente = self.primero
                nuevo.siguiente.anterior = nuevo
                self.primero = nuevo
            #ordenamos por nombre si primero es mayor que anterior y guarda delante de el 
            else:
                auxiliar = self.primero
                while ((auxiliar.siguiente is not None) and (auxiliar.siguiente.nombre.upper() < nuevo.nombre.upper())):
                    auxiliar = auxiliar.siguiente
    
                    nuevo.siguiente = auxiliar.siguiente

                    if auxiliar.siguiente is not None:
                        nuevo.siguiente.anterior = nuevo
 
                    auxiliar.siguiente = nuevo
                    nuevo.anterior = auxiliar
        #ordenamos por apellido si primero es mayor que anterior y guarda delante de el     
        else:
            auxiliar = self.primero
            
            while ((auxiliar.siguiente is not None) and
                   (auxiliar.siguiente.apellido.upper() < nuevo.apellido.upper())):
                auxiliar = auxiliar.siguiente
     
            
            nuevo.siguiente = auxiliar.siguiente

            if auxiliar.siguiente is not None:
                nuevo.siguiente.anterior = nuevo
 
            auxiliar.siguiente = nuevo
            nuevo.anterior = auxiliar

    def Buscar(self,numero):
        temp = self.primero
        while temp:
            if temp.numero==numero:
                print("Nombre Contacto: " + temp.nombre+"\nApellido: "+ temp.apellido+"\n Numero Telefonico: "+temp.numero)
                break
            temp = temp.siguiente
        if temp==None:
            print("-------------------------- Contacto No Registrado ------------------------")
            return False
        return True
    
    def generarGrafico(self):
        contador=0
        file = open("grafo.dot","w")
        file.write("digraph G{\n")
        temporal = self.primero
        while temporal != None:
                file.write(crearNodo(str(contador),"Nombre Contacto: " + temporal.nombre+"\nApellido: "+ temporal.apellido+"\n Numero Telefonico: "+temporal.numero, "box"))
                print("Nombre Contacto: " + temporal.nombre+"\nApellido: "+ temporal.apellido+"\n Numero Telefonico: "+temporal.numero)
                contador=contador+1
                temporal = temporal.siguiente
                print("-----------------------------------------------------------------------------------------------\n")
        for i in range(contador):
            file.write(unionNodo(str(i),str(i+1)))
            file.write(unionNodo(str(i+1),str(i)))
        file.write("}")
        file.close()
        os.system('dot -Tpng grafo.dot -o grafo.png')