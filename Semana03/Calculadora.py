class Calculadora:
    def sumar(self,a,b):
        return a + b
    def restar(self,a,b):
        return a - b
    def multiplicar(self,a,b):
        return a * b
    def dividir(self,a,b):
        if b != 0:
            return a / b
        else:
            return "no se puede divir entre 0"
while True:        
    print(f"Opciones:\n1-Sumar\n2-Restar\n3-Multiplicar\n4-Dividir\n5-Salir")

    option = int(input("Ingrese una opción "))
    a = float(input("Digite el primer numero "))
    b = float(input("Digite el segundo numero "))
    cal = Calculadora()
    if option >=1 and option <=5:
        if option == 1:
            suma = cal.sumar(a,b)
            print(f"La suma de {a} + {b} es: {suma}")
        elif option == 2:
            resta = cal.restar(a,b)
            print(f"La resta de {a} - {b} es: {resta}")
        elif option == 3:
            multi = cal.multiplicar(a,b)
            print(f"La multiplicación de {a} * {b} es: {multi}")
        elif option == 4:
            div = cal.dividir(a,b)
            print(f"La division de {a} / {b} es: {div}")
            break
        else:
            print("Gracias por usar la calculadora")