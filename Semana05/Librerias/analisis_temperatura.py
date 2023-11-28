# Abrir el archivo de temperaturas con la estructura with
with open('temperatura.txt', "r") as archivo: # r es para abrir en modo lectura
    # Leer los datos
    temperaturas = [float(linea.strip()) for linea in archivo]
    # 'for linea in archivo' se utiliza para recorrer el archivo linea por linea
    # 'linea.strip()' lo utilizamos para eliminar cualquier espacio en blanco que exista
    # 'float(...)' lo utilizamos para convertir cada linea en un tipo de dato decimal

# Imprimir los datos para validar que existen
for temp in temperaturas:
    print(temp)

# Calcular el promedio de temperaturas
print(f"El promedio es: {sum(temperaturas)/len(temperaturas)}")

# Calcular la temperatura máxima y miníma
