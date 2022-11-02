#Ejemplo en codigo
def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')


#Ejemplo basico
def suma():
    n1 = int(input('numero 1: '))
    n2 = int(input('numero 2: '))
    print(n1 + n2)
    print('Gracias por sumar'+n1)

try:
    suma()
except ValueError:
    print('Ese no es un numero')
except TypeError:
    print('Estas intentando concatenar tipos distintos')
else:
    print('Hicistes todo bien')
finally:
    print('Eso fue todo')


