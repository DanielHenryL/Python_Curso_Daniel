from zipfile import ZipFile

# Descomprimir
zip_abierto = ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()


# Comprimir
#mi_zip = ZipFile('archivo_comprimido.zip', 'w')
#mi_zip.write('mi_texto_A.txt')
#mi_zip.write('mi_texto_B.txt')

#mi_zip.close()
