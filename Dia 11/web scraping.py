from bs4 import BeautifulSoup
import requests
# Tarea: descargar todos los imagens de solo los cursos
url_cursos_img = 'https://www.escueladirecta.com/courses'
resultado = requests.get(url_cursos_img)
sopa = BeautifulSoup(resultado.text, 'lxml')
imagenes_todas = sopa.select('.course-box-image')
solo_img = []
for img in imagenes_todas:
    solo_img.append(img['src'])
for i in solo_img:
    f = open(f'Imagenes/{solo_img.index(i)+1}.jpg', 'wb')
    f.write(requests.get(i).content)
    f.close()


# Ejemplo con url a curso que
'''url_cursos = 'https://www.escueladirecta.com/courses'
reultado_1 = requests.get(url_cursos)
sopa_1 = BeautifulSoup(reultado_1.text, 'lxml')
imagenes = sopa_1.select('.course-box-image')[0]['src']
imagen_curso_1 = requests.get(imagenes)
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()'''


# Ejemplo con url a cursos traera todas las imagenes de cada curso
'''url_cursos = 'https://www.escueladirecta.com/courses'
reultado_1 = requests.get(url_cursos)
sopa_1 = BeautifulSoup(reultado_1.text, 'lxml')
imagenes = sopa_1.select('.course-box-image')
for img in imagenes:
    print(img)'''


# Ejemplo con url a un blog
'''url_blog = 'https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html'
resultado_2 = requests.get(url_blog)
sopa_2 = BeautifulSoup(resultado_2.text, 'lxml')

columna_lateral_derecha = sopa_2.select('.PopularPosts article')
for p in columna_lateral_derecha:
    print(p.getText())'''

# ejemplo basico
# titulo = sopa.select('p')[0].getText()
# print(titulo)
