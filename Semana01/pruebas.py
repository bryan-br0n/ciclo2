'''lado1 = float(input("Ingresa el primer lado del angulo -> "))
lado2 = float(input("Ingresa el segundo lado del angulo -> "))
lado3 = float(input("Ingresa el tercer lado del angulo -> "))

if lado1 == lado2 and lado2 == lado3:
    print("Tu triangulo es 'Equilatero'")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Tu triangulo es 'Isósceles'")
else:
    print("Tu triangulo es 'Escaleno'")'''

def sumar_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

try:
    numero_ingresado = int(input("Ingrese un número entero positivo: "))
    if numero_ingresado < 0:
        print("El número ingresado debe ser positivo.")
    else:
        resultado = sumar_digitos(numero_ingresado)
        print("La suma de los dígitos del número ingresado es:", resultado)
except ValueError:
    print("Por favor, ingrese un número válido.")