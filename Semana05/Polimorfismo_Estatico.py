class Utilidades:

    # Polimorfismo Estatico consiste en utilizar un mismo nombre de funcion
    # pero que se nos de la facilidad de enviar n cantidad de parametros
    def suma(self, x, y, z=None, a=None):
        if(z != None):
            print(f"El resultado es {str(x + y + z)}")
        else:
            print(f"El resultado es {str(x+y)}")

util = Utilidades()
print(util.suma(5,5))
