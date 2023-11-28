#3_Verificación de Contraseña:
print("Bienvenido al programa 'verificación de contraseña'")

contraseña1 = "secreto123"
contraseña = input("digita la contraseña\n")

if contraseña1 == contraseña:
    print("Acceso permitido")
else:
    print("Acceso denegado")