#10_Numeros pares en un rango
print("Programa 'Numeros pares en un rango'")

print("Ingresa dos numeros dentro del rango 5-35")
lim1 = int(input("Ingresa el primer numero -> "))
lim2 = int(input("Ingresa el segundo numero -> "))

for z in range(lim1,lim2,1):
    if z % 2 == 0:
        print(z)