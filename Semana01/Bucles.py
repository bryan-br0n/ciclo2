'''#Conteo Regresivo
numero = int(input("Ingresa un numero entero positivo -> "))

while numero >= 1:
    print("Cuenta regresiva... {0}".format (numero))
    numero -= 1


NUMERO_SECRETO = 123
cntr = 1

while True:
    numero = int(input("Escribe el numero que crees que es el correcto -> "))

    if numero == NUMERO_SECRETO:
        print("Felicidades acertaste. Numero de intento {}".format(cntr))
        break
    else:
        cntr += 1



#Conteo de caracteres en una cadena:
mensaje = input("Ingrese una frase corta:\n")
caracter = input("Ingrese el caracter a buscar:\n")
cntr = 0

for i in mensaje:
    if i == caracter:
        cntr += 1

print(f"El caracter '{caracter}'se repite {cntr} veces")

'''
for j in range(1,12,2):
    print(j)



