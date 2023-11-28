#11_Comprobación de validez de usuario
print("Programa 'Validez de usuario'")

nomUsu = input("Ingresa tu nombre de usuraio -> ")
edad = int(input("Ingresa tu edad -> "))

if nomUsu != "" and edad >= 18:
    print("Tu usuario es valido")
else:
    print("Tu usuario no es valido")