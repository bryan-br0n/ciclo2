# 1- Clasificacion de clificaciones
# nota = int(input("Ingrese la nota del estudiante"))

# if nota >=0 and nota <= 100:
#     if nota >=90 and nota <= 100:
#         print("La nota del estudiante es 'A' ")
#     elif nota >=8- and nota <= 89:
#         print("La nota del estudiante es 'B' ")
#     elif nota >=70 and nota <= 79:
#         print("La nota del estudiante es 'C' ")
#     elif nota >=60 and nota <= 69:
#         print("La nota del estudiante es 'D' ")
#     elif nota >=0 and nota <= 59:
#         print("La nota del estudiante es 'F' ")
# else:
#     print("La nota ingresada no esta en la escala del 1 al 100")

# 2- Deteremina un numero mayor
# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))
# num3 = int(input("Ingrese el tercer numero: "))
# numero_mayor = 0
# if num1 > num2:
#    if num1 > num3:
#        numero_mayor = num1
#    else:
#        numero_mayor = num3
    
# else:
#     if num2 > num3:
#        numero_mayor = num2
#     else:
#         numero_mayor = num3
# print(f"El número mayor es: {numero_mayor}")
   
   
   
# 3-Verrificacion de contraseñas
# password = input("Ingrese su contraseña secreta")
# password_secret = "Secreto123"

# while True:
#     if password == password_secret:
#         print("la contraseña Ingresada es !!Correcta!!")
#         break
#     else:
#         print("La Contraseña es !!!Invalida!!!")
#         return True
        
#4-Comparacion de numero
# num1 = int(input("Ingrese el primer numero"))
# num2 = int(input("Ingrese el segundo numero"))

# if num1 == num2:
#     print(f"{num1} Es igual a  {num2}")
# elif num1 > num2:
#     print(f"{num1} Es Mayor a  {num2}")
# else:
#     print(f"{num1} Es Menor a  {num2}")


# 5-Clasificación de Edades:

# edad = int(input("Ingrese la edad a calificar"))

# if edad >= 0 and edad <= 12:
#     print("Niño")
# elif edad >= 13 and edad <= 19:
#     print("Adolecente")
# elif edad >= 20 and edad <= 39:
#     print("Adulto Joven")
# elif edad >= 40 and edad <= 59:
#     print("Adulto")
# elif edad >= 60:
#     print("Adulto Mayor")


# 6- Clasificación de Triángulos

# long1 = float(input("Ingrese la primera longitud"))
# long2 = float(input("Ingrese la segunda longitud"))
# long3 = float(input("Ingrese la tercera longitud"))

# if long1 == long2 and long1 == long3:
#     print("El triángulo es 'Equilatero'")
# elif long1 == long2 or long1 == long3 or long2 == long3:
#     print("El triángulo es 'Isoceles'")
# else:
#     print("El triángulo es 'Escaleno'")

## 7 Suma de Dígito ##
# numero = 0
# while True:
#     numero = int(input("Ingrese un numero entero positivo: "))
#     if numero > 0:
#         break
#     else:
#         print("El numero Ingresado no es positivo: ")
# suma = 0
# while numero >= 0:
#     suma += numero
#     numero -= 1
# print(f"La suma de los digitos del numero ingresado es: {suma}")     

## 8 Suma de Dígitos ##
# suma = 0 
# while True:
#      numero = int(input("Ingrese un numero entero positivo: "))
#      if numero > 0:
#         suma += numero
#      else:
#         print("El numero Ingresado no es positivo: ")
#         break
# print(f"La suma de los numeros Ingresados es: {suma}")

## 9- Tabla de Multiplicar ##
# numero = int(input("Ingrese un numero entero: "))
# cntr = 1
# for x in range(cntr, 11, 1):
#     print(f"{numero} X {cntr} = {numero * cntr}")
#     cntr += 1
        
## 10- Números Pares en un Rango ##
# limite1 = int(input("Ingrese su primer numero: "))
# limite2 = int(input("Ingrese su segundo numero: "))

# for x in range(limite1,limite2,1):
#     if x % 2 == 0:
#         print(x)

## 11- Comprobación de Validez de Usuario ##
# nombre = input("Ingrese el nombre de usuario: ")
# edad = int(input("Ingrese su edad: "))

# if nombre != "" and edad >= 18:
#     print("Este usuario es !Valido!")
# else:
#     print("Este usuario !No es Valido!")

## 12- . Acceso al Sistema ##
# NAME = "admin"
# PASSWORD = "12345"
# nombre_usuario = input("Ingrese su nombre de usuario: ")
# contra = input("Ingrese su contraseña de usuario: ")
# if nombre_usuario == NAME and contra == PASSWORD:
#     print(f"Bienvenido al Sistema {NAME}")
# else:
#     print("Las Credenciales !!no son correctas!!")

## 13- Ingreso a una Película ##
# edad = int(input("Ingrese la edad: "))
# acompanado = input("¿Está acompañado de un adulto? (si/no): ")
# if edad >= 18 or acompanado.lower() == "si":
#      print("Acceso permitido a la película.")
# else:
#     print("Acceso restringido a la película.")

## 14- Concesión de Préstamo ##

# salario = float(input("Ingrese su salario anual: "))
# years_empleo = int(input("Ingrese el numero de años de empleo actual: "))

# if salario > 30000 or years_empleo >= 2:
#     print("Préstamo aprobado.")
# else:
#     print("Préstamo no aprobado.")

## 15- Acceso a una Función ##

#def valid_loggin(boolean):
#    if not boolean:
#        print("Inicia session para acceder a la funcion")
#    else:
#        print("Haz iniciado session, puedes acceder a la funcion")
    
# valid_loggin(False)

## 16- Verificación de Edad ##
# edad = int(input("Ingrese su edad: "))
# if not edad >= 18:
#     print("!!Debe ser mayor de edad para acceder a cierta funcionalidad!!")
# else:
#     print("Tienes acceso a todas las funcionalidades")