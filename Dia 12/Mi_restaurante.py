from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox
operador = ''
precios_comida = [5, 6, 7, 8, 9, 10, 11, 12]
precios_bebida = [1, 2, 3, 4, 5, 6, 2, 9]
precios_postre = [5, 8, 3, 9, 5, 1, 4, 7]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)
    operador = resultado


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if texto_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
                cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    y = 0
    for c in cuadros_bebida:
        if variables_bebida[y].get() == 1:
            cuadros_bebida[y].config(state=NORMAL)
            if texto_bebida[y].get() == '0':
                cuadros_bebida[y].delete(0, END)
                cuadros_bebida[y].focus()
        else:
            cuadros_bebida[y].config(state=DISABLED)
            texto_bebida[y].set('0')
        y += 1
    z = 0
    for c in cuadros_postre:
        if variables_postre[z].get() == 1:
            cuadros_postre[z].config(state=NORMAL)
            if texto_postre[z].get() == '0':
                cuadros_postre[z].delete(0, END)
                cuadros_postre[z].focus()
        else:
            cuadros_postre[z].config(state=DISABLED)
            texto_postre[z].set('0')
        z += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuesto = sub_total * 0.18
    total = sub_total + impuesto

    var_costo_comida.set(f'S/.{round(sub_total_comida,2)}')
    var_costo_bebida.set(f'S/.{round(sub_total_bebida,2)}')
    var_costo_postre.set(f'S/.{round(sub_total_postre,2)}')
    var_subtotal.set(f'S/.{round(sub_total,2)}')
    var_impuestos.set(f'S/.{round(impuesto,2)}')
    var_total.set(f'S/.{round(total,2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N° - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'{num_recibo}\t\t {fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*54 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-'*64+'\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x].upper()}\t\t{comida.get()}\t'
                                     f'S/. {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    y = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[y].upper()}\t\t{bebida.get()}\t'
                                     f'S/. {int(bebida.get()) * precios_bebida[y]}\n')
        y += 1

    z = 0

    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[z].upper()}\t\t{postre.get()}\t'
                                     f'S/. {int(postre.get()) * precios_postre[z]}\n')
        z += 1

    texto_recibo.insert(END, f'-' * 64 + '\n')
    texto_recibo.insert(END, f'Costo de la Comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida:\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Postre:\t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 64 + '\n')
    texto_recibo.insert(END, f'Sub Total:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos:\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 54)
    texto_recibo.insert(END, '\t GRACIAS!')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo a sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x600+0+0')

# Para evitar maximizar
aplicacion.resizable(False, False)

# Titulo de la venta
aplicacion.title('Mi restaurante - Sistema de facturacion')

# Color de fondo de la ventana
aplicacion.config(bg='CadetBlue', padx=17)

# Panel superior, bd(borde), relievef(flat,raised, sunken, groove, ridge)
panel_superior = Frame(aplicacion, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de ventas', fg='white',
                        font=('Dosis', 50), bg='CadetBlue', width=25)
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel Costos
panel_costo = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='CadetBlue4', padx=50)
panel_costo.pack(side=BOTTOM)


# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT)
panel_calculadora.pack(side=TOP)

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT)
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT)
panel_botones.pack()

# Comidas
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'cebiche', 'pizza', 'tallarines', 'Causa']
lista_bebidas = ['agua', 'pisco', 'cerveza', 'vino', 'Champan', 'Jugo', 'Ron', 'Corona']
lista_postres = ['gelatina', 'manzana', 'platano', 'helado', 'flan', 'pastel', 'pastel2', 'pastel3']

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 15),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)
    # Crear los cuadros de entrado
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # Crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 15),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)
    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Generar items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:
    # Crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 15),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)
    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
# Comida
etiqueta_costo_comida = Label(panel_costo,
                              text='Costo Comida',
                              font=('Dosis', 12),
                              bg='CadetBlue4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costo,
                           font=('Dosis', 12),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)
# Bebida
etiqueta_costo_bebida = Label(panel_costo,
                              text='Costo Bebida',
                              font=('Dosis', 12),
                              bg='CadetBlue4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costo,
                           font=('Dosis', 12),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)
# Postre
etiqueta_costo_postre = Label(panel_costo,
                              text='Costo Postres',
                              font=('Dosis', 12),
                              bg='CadetBlue4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costo,
                           font=('Dosis', 12),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)
# SubTotal
etiqueta_subtotal = Label(panel_costo,
                          text='Subtotal',
                          font=('Dosis', 12),
                          bg='CadetBlue4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costo,
                       font=('Dosis', 12),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)
# Impuesto
etiqueta_impuestos = Label(panel_costo,
                           text='Impuesto',
                           font=('Dosis', 12),
                           bg='CadetBlue4',
                           fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costo,
                        font=('Dosis', 12),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)
# Total
etiqueta_total = Label(panel_costo,
                       text='Total',
                       font=('Dosis', 12),
                       bg='CadetBlue4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costo,
                    font=('Dosis', 12),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)
# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14),
                   fg='white',
                   bg='CadetBlue4',
                   bd=1,
                   width=6,
                   padx=5)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
# area recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12),
                    bd=1,
                    width=36,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)
# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 20),
                          width=22,
                          bd=1,
                          )
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'Result', 'Borrar', '0', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16),
                   fg='white',
                   bg='CadetBlue4',
                   bd=1,
                   width=6)
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    columna += 1
    if columna == 4:
        fila += 1
        columna = 0
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))
# Evitar que la ventana no se cierre
aplicacion.mainloop()
