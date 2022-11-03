from numeros import *


class Cliente:
    def __init__(self, nombre,codigo_operacion):
        self.nombre = nombre
        self.codigo_operacion = codigo_operacion

    def __str__(self):
        return self.nombre


def crear_cliente(categoria):

    nombre = input('Ingrese su nombre: ')

    if categoria == 'P':
        codigo = next(per)
        print(codigo)
    elif categoria == 'F':
        codigo = next(far)
        print(codigo)
    else:
        codigo = next(cos)
        print(codigo)
    Cliente(nombre, codigo)


def inicio():
    print('*'*50)
    print('*'*17 + "Consola de turno" + "*"*17)
    print('*'*50)
    print('\n')
    opciones = ['P', 'F', 'C']
    print('A que categoria quiere el turno: ')
    print('[P].Categoria perfume')
    print('[F].Categoria farmacia')
    print('[C].Categoria cosmeticos')
    print('[S].Salir')

    while True:
        opcion = input('Ingrese la letra "P, F o C": ').upper()

        if len(opcion) == 1 and opcion in opciones:
            crear_cliente(opcion)
        elif opcion == 'S':
            break
    print('Gracias')


inicio()
