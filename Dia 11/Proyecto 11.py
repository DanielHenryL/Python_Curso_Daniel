from bs4 import BeautifulSoup
import requests
# Solucion al proyecto
url_bases = 'https://books.toscrape.com/catalogue/page-{}.html'
title_cinco_estrellas = []
for i in range(1, 20):
    # Peticion a la url base
    resultado_1 = requests.get(url_bases.format(i))
    # Transfomar el resultado en algo entendible para python
    sopa = BeautifulSoup(resultado_1.text, 'lxml')
    # Total de libros
    libros = sopa.select('.product_pod')

    for libro in libros:
        # Para 4 o 5 estrellas
        # if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) !=0:
        estrellas = libro.select('.star-rating.Five')
        if len(estrellas) > 0:
            title = libro.select('a')[1]['title']
            title_cinco_estrellas.append(title)

print('*' * 50)
print('\n')
print(f'Cantidad de libros con cinco estrellas: {len(title_cinco_estrellas)}')
print('Los titulos son: \n')
for title in title_cinco_estrellas:
    print(title)
print('\n')
print('*' * 50)

# Guia del proyecto

'''# url base del sitio
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
# Peticion a la url base
resultado = requests.get(url_base.format('1'))
# Transfomar el resultado en algo entendible para python
sopa = BeautifulSoup(resultado.text, 'lxml')
# Total de libros
libros = sopa.select('.product_pod')
# Cantidad de estrellas
ejemplo = libros[4].select('.star-rating.Five')
# Buscar title
buscar_title = libros[0].select('a')[1]['title']'''
# print(buscar_title)
'''for n in range(1, 15):
    print(url_base.format(n))'''
