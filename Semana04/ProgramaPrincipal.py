import Calculadora as cal
import Fecha as fecha

#try catch

while True:
    print("Bienvenido a tu Calculadora")
    print("\nElige una opción a ingresar")
    print("1. Sumar")
    print("2. Restar")
    print("3. salir")
    opcion = int(input())
    if opcion == 1:
        a = int(input("Ingrese el primer valor -> "))
        b = int(input("Ingrese el segundo valor -> "))
        resultado = cal.sumar(a,b)
        print(f"El resultado es: {resultado}"
              f"\nOperacion realizada en la fecha: {fecha.obtener_fecha_actual()}")
    elif opcion == 2:
        a = int(input("Ingrese el primer valor -> "))
        b = int(input("Ingrese el segundo valor -> "))
        resultado = cal.restar
        print(f"El resultado es: {resultado}"
              f"\nOperacion realizada en la fecha: {fecha.obtener_fecha_actual()}")
    elif opcion == 3:
        print("Gracias por ocupar la Calculadora")
        break
    else:
        print("Opción invalida, vuelva a intentar")

