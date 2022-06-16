#CUADROS


class Cuadro:
    def __init__(self, id, imagen):
        self.id = id
        self.imagen = imagen

    def __str__(self):
        return f'\t ****Cuadro**** \n' \
               f'\t ID:{self.id} \n' \
               f'\t Imagen: {self.imagen} \n' \


class CuadroNuevo:
    def __init__(self, medidas, imagen):
        self.medidas = medidas
        self.imagen = imagen

    def __str__(self):
        return f'\t ======= Tu cuadro personalizado es: ======= \n' \
               f'\t Medidas:{self.medidas} \n' \
               f'\t Imagen: {self.imagen} \n'