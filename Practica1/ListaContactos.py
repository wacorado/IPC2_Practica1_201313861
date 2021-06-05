from NodoContacto import Contacto

class ListaContactos:
    def __init__(self):
        self.primero = None
        #self.ultimo = None
    
    def AgregarAlFinal(self, nombre, apellido, numero):
        nuevo = Contacto(nombre, apellido, numero)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
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

    
    def mostrarLista(self):
        temporal = self.primero
        while temporal is not None:
            print("Nombre: "+ temporal.nombre+" \nApellido: "+temporal.apellido+" \nNumero: "+temporal.Numero)
            print("\n")
            temporal = temporal.siguiente

    def imprimirAgenda(self):
        temporal = self.primero
        while temporal != None:
                print("Nombre Contacto: " + temporal.nombre+"\nApellido: "+ temporal.apellido+"\n Numero Telefonico: "+temporal.numero)
                temporal = temporal.siguiente
                print("-----------------------------------------------------------------------------------------------\n")

		## printing the data in normal order
		#print("Normal Order: ", end='')
	    #temporal = self.head
		#while temporal != None:
			#print(temp_node.data, end=' ')
			#temp_node = temp_node.next
		#print()

		## printing the data in reverse order using previous pointer
		#print("Reverse Order: ", end='')

		## getting the last node
		#last_node = self.head
		#while last_node.next != None:
			#last_node = last_node.next

		#temp_node = last_node
		#while temp_node != None:
			#print(temp_node.data, end=' ')
			#temp_node = temp_node.prev
		#print() 