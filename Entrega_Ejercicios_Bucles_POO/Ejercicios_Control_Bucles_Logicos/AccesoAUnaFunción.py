#15_Accesso a una función
print("Programa 'Acceso a una función'")

def valid_loggin(boolean):
    if not boolean:
        print("Inicia sesión para acceder a la funcion")
    else:
        print("Haz iniciado sesion, puedes acceder a la funcion")
    
valid_loggin(False)