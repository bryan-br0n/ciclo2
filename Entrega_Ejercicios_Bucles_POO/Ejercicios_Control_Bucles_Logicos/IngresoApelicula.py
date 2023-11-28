#13_Ingreso a una pelicula
print("Programa 'Acceso a una película'")

edad = int(input("Ingresa tu edad -> "))
acom = input("Te acompaña un adulto? ")

if edad >= 18 or acom == "si":
    print("Puedes pasar a ver tu pelicula")
else:
    print("Acceso restringido")