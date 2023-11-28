#5_Clasificación de Edades:
print("Bienvenido al programa 'Clasificación de dades'")

edad = int(input("Ingresa tu edad -> "))

if edad >= 0 and edad <= 12:
    print("Te encuentras en el rango de 'niño'")
elif edad >= 13 and edad <=19:
    print("Te encuentras en el rango de 'Adolescente'")
elif edad >= 20 and edad <= 39:
    print("Te encuentras en el rango de 'Adulto joven'")
elif edad >= 40 and edad <= 59:
    print("te encuentras en el rango de 'Adulto'")
else:
    print("Te encuentras en el rango de 'Adulto mayor'")