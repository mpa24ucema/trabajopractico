import random

def generador_numero_de_compra():
    return str(random.randint(1000000, 9000000))


class Client:

    def __init__(self, nombre, apellido, numero_telefonico, email, numero_de_compra):

        self.nombre = nombre
        self.apellido = apellido
        self.numero_telefonico = numero_telefonico
        self.email = email
        self.numero_de_compra = numero_de_compra


    def serialize(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'numero_de_telefono': self.numero_telefonico,
            'email': self.email,
            "numero_de_compra": self.numero_de_compra
        }
