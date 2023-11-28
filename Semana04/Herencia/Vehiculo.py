#Clase vehiculo sera clase padre
class Vehiculo:
    #inicializamos nuestras variables en el metodo __init__
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    #creamos un metodo para mostras información del vehiculo
    def describir(self):
        return f"Este es un {self.marca} {self.modelo}"
    

