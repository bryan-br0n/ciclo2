class CuentaBancaria:

    def __init__(self, titular, saldo_inicial, numero_cuenta):
        self.titular = titular
        self.saldo = saldo_inicial
        self.numero_cuenta = numero_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Deposito de {cantidad} realizado. Saldo actual: {self.saldo}")
        

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print(f"Saldo insuficiente")


#Crear la instancia de la clase

cuenta1 =CuentaBancaria("Ana", 30, 2004178230)
cuenta2 = CuentaBancaria("Carlos", 15, 20301528)

#Interaccion entre objetos
cuenta1.depositar(100)
cuenta2.retirar(50)