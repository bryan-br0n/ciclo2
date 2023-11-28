#6_Clasificación de Triángulos:
print("Bienvenido al programa 'Clasificación de triangulos'")

lado1 = float(input("Ingresa el primer lado del angulo -> "))
lado2 = float(input("Ingresa el segundo lado del angulo -> "))
lado3 = float(input("Ingresa el tercer lado del angulo -> "))

if lado1 == lado2 and lado2 == lado3:
    print("Tu triangulo es 'Equilatero'")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Tu triangulo es 'Isósceles'")
else:
    print("Tu triangulo es 'Escaleno'")