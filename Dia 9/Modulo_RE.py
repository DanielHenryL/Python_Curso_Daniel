import re


def verificar_email(email):
    patron10 = r'\w+@\w+\.com'
    buscar10 = re.search(patron10, email)
    if buscar10:
        print('Ok')
    else:
        print("La dirección de email es incorrecta")


verificar_email('daniel@gmail.com.br')

# 6 Ejercicio basico
texto6 = 'No atendemos los lunes por la tarde'
buscar4 = re.findall(r'\S+', texto6)
print(buscar4)

# 5 Ejercico basico
texto5 = 'No atendemos los lunes por la tarde'
buscar3 = re.search(r'\D$', texto5)
print(buscar3)

# 4 Ejercico Basico, se entiende que si un patron se encuentra al comienzo del texto
texto4 = 'No atendemos los lunes por la tarde'
buscar2 = re.search(r'^No', texto4)
print(buscar2)

# 3 Ejercicio basico
texto3 = 'No atendemos los lunes por la tarde'
buscar1 = re.search(r'....demos', texto3)
print(buscar1)

# 2 Ejercicio basico
texto2 = 'No atendemos los lunes por la tarde'
buscar = re.search(r'lunes|martes',texto2)
print(buscar)


# 1 Ejercio basico
clave = input('Clave: ')
patron_1 = r'\D{1}\w{7}'
chequear = re.search(patron_1, clave)
print(chequear.group())


# Como construir un patron
texto1 = 'llama al 564-525-6588 llama ya mismo'
patron0 = r'\d\d\d-\d\d\d-\d\d\d\d'
resultado1 = re.search(patron0, texto1)
print(resultado1.group())
# Cuantificado seria r'\d{3}\d{3}\d{4}'
patron1 = r'\d{3}-\d{3}-\d{4}'
resultado2 = re.search(patron1, texto1)
print(resultado2.group())
# Compilado, para poder acceder a cada grupo del caracter
patron2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado3 = re.search(patron2, texto1)
print(resultado3.group(1))

# Como usar un patron

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'
patron = 'ayuda'
# finditer, iterar cada elemento
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

# findall, busca todas las coicidencias
busqueda = re.findall(patron, texto)
print(len(busqueda))

# Search busca la primera coicidencia
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

