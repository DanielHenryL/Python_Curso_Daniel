def generador(name):
    x = 1
    yield f'{name}-{x}'

    x += 1
    yield f'{name}-{x}'

    x += 1
    yield f'{name}-{x}'


g = generador('daniel')
print(next(g))
print(next(g))
print('Hola mundo')
print(next(g))

"""Generador ejm basico"""


def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x*10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
