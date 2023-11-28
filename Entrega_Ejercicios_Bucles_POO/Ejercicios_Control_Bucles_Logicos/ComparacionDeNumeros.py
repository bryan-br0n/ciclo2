#4_Comparación de Números:
print("Bienvenido al programa 'comparación de numeros'")

num1 = int(input("Ingresa un numero entero -> "))
num2 = int(input("Ingresa otro numero entero -> "))

if num1 > num2:
    mayor = num1
    print("El numero mayor es ", mayor)
elif num2 > num1:
    mayor = num2
    print("El numero mayor es ", mayor)
else:
    print("Ambos numeros son iguales")