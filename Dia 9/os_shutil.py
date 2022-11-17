import os, shutil
from pathlib import Path
# shutil
base = Path.home()

ruta = Path(base,'Carpeta_superior')

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')
# Elimina un directorio y su contenido de forma permanente e irreversible
# shutil.rmtree()


# Mover 
# shutil.move('prueba.txt', 'ruta')

# Recordando
# print(os.getcwd())
# archivo = open('prueba.txt', 'w')
# archivo.write('Hola como estas')
# archivo.close()
# print(os.listdir())

