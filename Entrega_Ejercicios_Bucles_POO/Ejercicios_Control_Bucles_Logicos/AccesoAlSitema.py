'''#12_Acesso al sistema
print("Programa 'Acceso al sistema'")

usuario = "admin"
contra = 12345

Usuario = input("Ingresa el nombre de usuario -> ")
Contra = int(input("Ingresa la contraseña -> "))

if usuario == Usuario and contra == Contra:
    print("Bienvenido al sistema :)")
else:
    print("tu contraseña o usuario es incorrecto")'''

class Calculadora:
    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "No se puede dividir entre cero"
while True:
    #Menu de opciones de la calculadora#
    print(f"Opciones:\n1-Suma\n2-Resta\n3-Multiplicacion\n4-Division\n5-Salir")
    #Fin Menu de opciones de la calculadora#
    try:
        #Ingreso de opcion del menu 
        option = int(input("Ingrese una de las opciones: "))
        #Captura de datos#
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if option >= 1 and option <= 5:
            calculadora = Calculadora()
            if option == 1:
                suma = calculadora.sumar(num1,num2)
                print(f"La suma de {num1} + {num2} es: {suma}")
            elif option == 2:
                resta = calculadora.restar(num1,num2)
                print(f"La resta de {num1} - {num2} es: {resta}")
            elif option == 3:
                multi = calculadora.multiplicar(num1,num2)
                print(f"La multiplicacion de {num1} * {num2} es: {multi}")
            elif option == 4:
                division = calculadora.dividir(num1,num2)
                try:
                   if division.isdigit():
                       print(f"La division de {num1} / {num2} es: {division}")
                   else:
                       print(f"{division}")
                except ValueError:
                    print(f"{division}")
            else:
                print("!!Gracias por utlizar su calculadora!!")
                print("Cerrando Programa...")
                break
        else:
            print("!!Debe ingresar una valor de las opciones en pantalla!!")
    except ValueError:
        print("debe ingresar un valor numerico.\nIntentalo otra vez!!")