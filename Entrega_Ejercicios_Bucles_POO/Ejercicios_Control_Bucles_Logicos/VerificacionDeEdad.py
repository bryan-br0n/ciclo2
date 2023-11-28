#16_Verificacion de edad
print("Programa 'verificación de edad'")

edad = int(input("Ingresa tu edad -> "))

if not edad >= 18:
    print("Debes ser mayor de edad para acceder.")
else:
    print("Puedes acceder.")