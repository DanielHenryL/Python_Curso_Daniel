from collections import Counter, defaultdict, namedtuple, deque


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    print(k)
    print(v)
    print(d)
    d[k].append(v)
print(d.items())


# tuplas con nombre
Persona = namedtuple('Persona',['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.altura)
print(ariel[0])


# crear una llave:valor usando defaultdict
mi_dic = defaultdict(lambda: 'nada')
mi_dic['dos'] = 'verde'
mi_dic['uno'] = 'azul'
mi_dic['tres'] = 'rojo'
print(mi_dic['cuatro'])
print(mi_dic)


# counter en numeros
numeros = [4, 5, 6, 8, 4, 5, 6, 8, 4, 1, 1, 2, 3, 4, 5, 6, 8, 7, 9]
print(Counter(numeros))

# Counter de una palabra
print(Counter('missisipi'))

# Counter de una frase
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))

# Metodos de un Counter
serie = Counter(numeros)
print(serie.most_common())  # most_common(1) quiere decir el que mas se repite, y 2 los dos mas q se repiten

# Elimina los repetidos
serie = Counter(numeros)
print(list(serie))
