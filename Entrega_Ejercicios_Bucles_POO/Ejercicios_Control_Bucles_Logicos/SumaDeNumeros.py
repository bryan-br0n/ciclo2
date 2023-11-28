#8_suma de numeros
print("Bienvenido al programa 'Suma de numeros'('para parar escribe uno negativo')")

suma = 0
num = int(input("Ingrese un numero entero positivo\n"))

while num >= 0:
    suma += num
    num = int(input("Ingrese otro numero\n"))
print("La suma total es: ", suma)

