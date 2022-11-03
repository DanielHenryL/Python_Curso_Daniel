def numero_generador(cate):

    if cate == 'P':
        for p in range(1, 100):
            yield f'{cate}-{p}'
    elif cate == 'F':
        for f in range(1, 100):
            yield f'{cate}-{f}'
    elif cate == 'C':
        for c in range(1, 100):
            yield f'{cate}-{c}'
    else:
        print(f'No se encontro la categoria : {cate}')
        return


per = numero_generador('P')
far = numero_generador('F')
cos = numero_generador('C')


def descripcion(funcion,cliente):
    print(f'{cliente} su turno es:')
    print(funcion)
    print('Aguarde y sera atendido')

