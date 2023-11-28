#14_Concesión de prestamo
print("Programa 'Concesión de prestamo'")

salario = float(input("Ingresa tu salario anual -> "))
años = int(input("¿Cuantos años has trabajado? "))

if salario > 30000 or años >= 2:
    print("Tu prestamo ha sido aprobado")
else:
    print("Tu prestamo no puede ser aprobado")