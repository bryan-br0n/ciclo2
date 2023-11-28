#Programa para sumar digito
num = int(input("Ingresa un numero entero positivo -> "))

suma = 0
while num > 0:
    # al dividir el numero entre 10 lo que se logra es extraer el ultimo numero
    # y ese numero se guarda en la variable digito
    digito = num % 10
    # aqui se suma el digito sacado de la variable anterior
    suma += digito
    # con esta variable se elimina el ultimo digito de la variable 'num'
    num //= 10
print("La suma de tus digitos es: ",suma )