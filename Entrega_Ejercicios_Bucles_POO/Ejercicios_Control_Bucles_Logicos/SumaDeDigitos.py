#Programa para sumar digito
num = int(input("Ingresa un numero entero positivo -> "))

suma = 0
while num > 0:
    # al dividir el numero entre 10 lo que se logra es extraer el ultimo numero
    # y ese numero se guarda en la variable digito
    digito = num % 10
    # aqui se suma el digito sacado de la variable anterior
    suma += digito
    num //= 10
print("La suma de tus digitos es: ",suma )


'''#Solicitar al usuario ingresar un número entero positivo
digitos = []
while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        numero_str = str(numero)
        
        for num in numero_str:
            digitos.append(int(num))
            
        print(f"La suma de los digitos del valor ingresado es: {sum(digitos)}")
        break

    except ValueError:
        print("!!Debe Ingresar un numeo entero positivo,Vuelva a Intentarlo!!")
print("Fin del Programa")'''