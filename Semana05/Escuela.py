class Estudiantes:
    def __init__(self, nombre, edad,):
        self.nombre = nombre
        self.edad = edad
        self. calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)
        pass
    def calcular_promedio(self):
        cntr = 0
        suma = 0
        for i in self.calificaciones:
            suma += i
            cntr += 1
        return f"El promedio de {self.nombre} es {sum(self.calificaciones)/len(self.calificaciones)} y la nota mayor es: {max(self.calificaciones)}"
        
    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\n{Estudiantes.calcular_promedio(self)}"
        pass
# Primero creamos los objetos estudiantes
estudiante_uno = Estudiantes("Juan", 18)
estudiante_dos = Estudiantes("Carlos", 18)

#Agregamos calificaciones a los objetos
estudiante_uno.agregar_calificacion(10)
estudiante_uno.agregar_calificacion(7)

estudiante_dos.agregar_calificacion(9)
estudiante_dos.agregar_calificacion(9)

#Mostrar promedio
estudiante_uno.calcular_promedio()
estudiante_dos.calcular_promedio()

#Mostrar informacion

print(estudiante_uno.mostrar_detalles())
print(estudiante_dos.mostrar_detalles())