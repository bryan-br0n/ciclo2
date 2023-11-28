#impprtamos la clase padre
from Vehiculo import Vehiculo

#Aplicamos herencia agregando la clse vehiculo
#como dependencia de nuestra clase coche
class Coche(Vehiculo):
    #Cuando creamos el metodo __init__ este
    #requiere que se envien los valores por defecto
    #de la propiedad marca y modelo que estan presentes
    #en la calse Vehiculo
    def __init__(self, marca, modelo, color, anio):
        super().__init__(marca, modelo)
        #inicializar las variables de la clase Coche
        self.color = color
        self.anio = anio

    def describir(self):
        return super().describir() + f" {self.color} año {self.anio}"
        