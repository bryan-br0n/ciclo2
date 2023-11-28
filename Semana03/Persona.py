class Persona:
    
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    
    def entrar_consultorio(self):
        pass

class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, genero, titulo, carnet):
        super().__init__(nombre, apellido, edad, genero)

class Doctor(Empleado):
    def __init__(self, nombre, apellido, edad, genero, titulo, carnet, sello):
        super().__init__(nombre, apellido, edad, genero, titulo, carnet)
        self.titulo = titulo
        self.carnet = carnet

    def entrar_consultorio(self):
        return "Dar una consulta al Paciente"
    
class Enfermera(Empleado):
    def __init__(self, nombre, apellido, edad, genero, titulo, carnet):
        super().__init__(nombre, apellido, edad, genero, titulo, carnet)

    def entrar_consultorio(self):
        return "Entregar expediente del paciente al doctor"

class Paciente(Persona):
    def __init__(self, nombre, apellido, edad, genero, telefono, direccion):
        super().__init__(nombre, apellido, edad, genero)
        self.telefono = telefono
        self.direccion = direccion
    
    def entrar_consultorio(self):
        return f"Pasar consulta con el medico"