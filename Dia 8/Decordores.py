def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


@decorar_saludo
def minusculas(texto):
    print(texto.lower())


mayusculas('daniel')
minusculas('HENRY')
