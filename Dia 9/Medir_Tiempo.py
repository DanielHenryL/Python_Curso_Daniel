
import time, timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(numero)
        contador += 1
    return lista


# Con timeit
# ciclo for
declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
'''
duracion = timeit.timeit(declaracion, mi_setup, number=1000000)
print(duracion)

# ciclo while
declaracion2 = '''
prueba_while(10)
'''
mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(numero)
        contador += 1
    return lista
'''
duracion2 = timeit.timeit(declaracion2, mi_setup2, number=1000000)
print(duracion2)
# Con time()
inicio = time.time()
prueba_for(10000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(10000)
final = time.time()
print(final - inicio)
