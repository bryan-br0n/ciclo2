PI = 3.14159

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return PI*(self.radio*self.radio)    
    
    def calcular_circunferencia(self):
        return 2*PI*self.radio
    

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        pass


#Instancia de la clase Circulo con un radio de 5
circulo = Circulo(5)
print("El area del circulo es: {}".format(circulo.calcular_area()))
print("La circunferencia del circulo: {}".format(circulo.calcular_circunferencia()))