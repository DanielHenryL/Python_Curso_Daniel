from os import system
class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f''' 
            Cliente: {self.nombre} - {self.apellido}
            Balance de Cuenta: {self.numero_cuenta} - S/{self.balance}
        '''

    def depositar(self, cantidad):
        self.balance += cantidad
        print('Deposito aceptado')

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print('Retiro Realizado')
        else:
            print('Fondos insuficiente')


def Bienvenida():
    print('Bienvenido al cajero automatico')


def crearCliente():
    nombre = input('Ingrese su nombre: ').capitalize()
    apellido = input('Ingrese su apelilido: ').capitalize()
    c_bancaria = int(input('Ingrese su cuenta bancaria: '))

    cliente = Cliente(nombre,apellido,c_bancaria)
    return cliente


def inicio():
    Bienvenida()
    cliente = crearCliente()
    print(cliente)
    opcion = 'x'
    while not opcion.isnumeric() or opcion not in range(1,4):
        print('Que operacion desea realizar: ')
        print('''[1]. Depositar''')
        print('''[2]. Retirar''')
        print('''[3]. Salir''')
        opcion = input('Ingrese una opcion: ')
        system('cls')
        if opcion == '1':
            cantidad_depositar = float(input('Ingrese la cantidad a depositar: '))
            cliente.depositar(cantidad_depositar) # primera forma
            #Cliente.depositar(cliente,cantidad_depositar) #Otra forma

        elif opcion == '2':
            cantidad_retirar = float(input('Ingrese la cantidad a retirar: '))
            cliente.retirar(cantidad_retirar)
            # Cliente.retirar(cliente,cantidad_retirar)
        elif opcion == '3':
            break

        print(cliente)
    print('Gracias por confiar en Banco Python')
inicio()