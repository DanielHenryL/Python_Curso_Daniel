import os
import re
import time
import math
from collections import Counter
from datetime import date
from pathlib import Path

ruta = Path('\\\wsl$\\Ubuntu-20.04\home\daniel\ProyectosDaniel\Python_Curso_Daniel\Dia 9\Proyecto dia 9\Mi_Gran_Directorio')
patron = r'N\w{3}-\d{5}'
fecha_hoy = date.today().strftime('%d/%m/%y')


def buscar_patron():
    dic = {}
    inicio_t = time.time()
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        for arch in archivos:
            archivo = Path(carpeta, arch)
            buscar = re.search(patron, archivo.read_text())
            if buscar:
                dic[arch] = buscar.group()
    final_t = time.time()
    medir_tiempo = final_t - inicio_t
    return dic.items(), medir_tiempo


def inicio():
    print('-'*40)
    print(f'Fecha de búsqueda: {fecha_hoy}\n')
    print('ARCHIVO\t\t\t Nmr. SERIE')
    print('-'*13+'\t '+'-'*10)
    dic, medir_t = buscar_patron()
    for key, value in dic:
        print(key,'\t', value)
    print('\n')
    print(f'Numeros encontrados: {Counter(dic).total()}')
    print(f'Duracion de la busqueda: {math.ceil(medir_t)} segundos')
    print('-' * 40)


inicio()
