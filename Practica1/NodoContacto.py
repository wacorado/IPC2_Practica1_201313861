class Contacto:
    def __init__(self, nombre, apellido, numero):
        self.nombre = nombre
        self.apellido = apellido
        self.numero= numero
        self.siguiente = None
        self.anterior = None