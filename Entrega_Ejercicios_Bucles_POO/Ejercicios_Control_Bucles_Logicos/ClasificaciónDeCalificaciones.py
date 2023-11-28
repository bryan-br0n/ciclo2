#1_Clasificación de Calificaciones
print("Bienvenido al sistema de clasificación de calificaciones")

calificacion = int(input("Ingresa tu calificación obtenida -> "))

if calificacion >= 90 < 100:
    print("La clasificación de tu calificación es: 'A'")
elif calificacion >= 80 < 90:
    print("La clasificación de calificación es: 'B'")
elif calificacion >= 70 < 80:
    print("La clasificación de tu calificación es: 'C'")
elif calificacion >= 60 < 70:
    print("La clasificación de tu calificacion es: 'D'")
elif calificacion >= 0 < 60:
    print("La clasificación de tu calificación es: 'F'")