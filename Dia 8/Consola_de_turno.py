from numeros import *
from os import system


class Cliente:
    def __init__(self, nombre,codigo_operacion):
        self.nombre = nombre.capitalize()
        self.codigo_operacion = codigo_operacion

    def __str__(self):
        return self.nombre


def crear_cliente(categoria):

    nombre = input('Ingrese su nombre: ')

    if categoria == 'P':
        codigo = next(per)
    elif categoria == 'F':
        codigo = next(far)
    else:
        codigo = next(cos)

    cliente = Cliente(nombre, codigo)
    return codigo, cliente


def inicio():
    print('*'*50)
    print('*'*17 + "Consola de turno" + "*"*17)
    print('*'*50)
    print('\n')
    opciones = ['P', 'F', 'C']

    while True:
        print('\n')
        print('A que categoria quiere el turno: ')
        print('[P].Categoria perfume')
        print('[F].Categoria farmacia')
        print('[C].Categoria cosmeticos')
        print('[S].Salir')
        opcion = input('Ingrese la letra "P, F o C": ').upper()
        system('cls')

        if len(opcion) == 1 and opcion in opciones:
            codigo,cliente = crear_cliente(opcion)
            descripcion(codigo,cliente)
        elif opcion == 'S':
            break
    print('Gracias')


inicio()
