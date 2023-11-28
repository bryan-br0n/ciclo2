#verificacion de numero Par: Escribe un programa que solicite al usuario
#ingresar un numero entero. Luego, verifica si el numero es par o impar y muestra
#un mensaje indicando el resultado.

'''numero = int(input("Ingresa un numero entero:\n"))

if numero % 2 == 0:
    print("Es un par")
if numero % 2 !=0:
    print("Es impar")



#EJERCICIO: EVALUACION DE EDAD
edad = int(input("Ingresa tu edad:\n"))

if edad >=18:
    print("Estas apto para votar en las elecciones")


precio = float(input("Ingresa el precio del articulo:\n"))
descuento = float(input("Ingresa el descuento asignado al articulo:\n"))

#si se cumple que el precio es mayor o igual a 1000 entra en el if(es True)
if precio >= 1000:
    #si se cumple ambas condiciones entonces se agrega 5% adicional
    if descuento >= 10:
        #realizamos el calculo del descuento y lo asignamos en una variable para mostrarlo
        descuento += 5
        resultado = precio - (precio*(descuento/100))
        print("Total: ${0}".format(resultado))
        #si no se cumple que el descuento
    else:
        resultado = precio - (precio*(descuento/100))
        print("Total: ${0}".format(resultado))
else:
    resultado = precio - (precio*(descuento/100))
        print("Total: ${0}".format(resultado))
        



#Evaluacion de Numero Positivo o Negativo
numero = float(input("Digite un numero:\n"))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo)
else:
    print("El numero es 0")


#Dia de la semana 
numero = int(input("Ingresa un numero:\n"))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
elif numero == 7:
    print("Domingo")
else:
    print("El numero ingresado esta fuera del rango de la semana [1-7]")


num1 = int(input("Dame el primer numero -> "))
num2 = int(input("Dame el segundo numero -> "))
num3 = int(input("Dame el tercer numero -> "))

print("tus numeros son", num1, num2, num3)

if num1 > num2 and num3:
    print("tu primer numero es mayor")
if num2 > num3 and num1:
    print("tu segundo numero es mayor")
if num3 > num2 and num1:
    print("tu tercer numero es mayor")
'''