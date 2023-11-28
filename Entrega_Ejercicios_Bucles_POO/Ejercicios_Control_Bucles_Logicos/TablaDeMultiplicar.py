#9_Tabla de multiplicar
print("Bienvenido al programa 'Tabla de multiplicar'")

num = int(input("Ingresa el numero a multiplicar -> "))
cntr = 1
for x in range(cntr,11,1):
    print(f"{num} x {cntr} = {num*cntr}")
    cntr +=1