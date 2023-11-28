#Primer paso para crear una clase es utilizar la abtracción

class CuentaBancariaV3:

    def __init__(self, titular, numero_cuenta, saldo):
        self.__titular = titular #'__' indicamos que la propiedad es privada
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular
        
    def set_titular(self, nombre):
        self.__titular = nombre

    def mostrar_informacion(self):
        print(f"Titular: {self.__titular}\nNumero de cuenta: {self.__numero_cuenta}\nSaldo: {self.__saldo}")

    def depositar(self, cantidad):
        self.__saldo += cantidad
        
    def retirar(self, cantidad):
        if(cantidad <= self.__saldo):
            self.__saldo -= cantidad
        else:
            print("No tiene fondos")



mi_cuenta = CuentaBancariaV3("Jorge", 40027613, 500)
mi_cuenta2 = CuentaBancariaV3("Ana", 7002013, 300)

mi_cuenta.mostrar_informacion()