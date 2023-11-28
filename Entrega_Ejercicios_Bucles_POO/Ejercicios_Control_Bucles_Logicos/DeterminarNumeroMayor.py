#2_Determinar numero mayor
print("Bienvenido al programa de determinar numero mayor")

num1 = int(input("Dame el primer numero -> "))
num2 = int(input("Dame el segundo numero -> "))
num3 = int(input("Dame el tercer numero -> "))

print("Tus numeros son", num1, num2, num3)

if num1 > num2 and num1 > num3: 
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
else:
    mayor = num3
print("El numero mayor es", mayor)