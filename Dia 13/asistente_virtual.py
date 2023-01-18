import pyttsx3  # Interprete para comunicarnos con el sistema
import speech_recognition as sr  # reconoce la voz y transformarla en texto
import pywhatkit  # Permite abrir sitios como youtube , wikipedia, etc
import yfinance as yf
import pyjokes  # Contar chistes
import webbrowser # Manejar el navegador de internet
import datetime
import wikipedia

# Opciones de voz
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


# Escuchar nuestro microfono y devolver el audi en texto
def transfomar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        r.pause_threshold = 0.8

        # Informar que comenzo la grabacion
        print('Ya puedes hablar')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language="es-per")

            # Prueba de que pudo ingresar
            print('Dijiste: ' + pedido.lower())

            # Devolver pedido
            return pedido

        # En caso no comprenda el audio
        except sr.UnknownValueError:
            # Mensaje que no entendio el audio
            print('OH no, no entendi el audio')

            # devolver error
            return 'Sigo esperando'

        # En caso de no resolver el pedido
        except sr.RequestError:

            # Mensaje que no pudo resolver la peticion
            print('OH no, no pude resolver la peticion')

            # devolver error
            return 'Sigo esperando'

        # Cualquier otro error
        except:
            # Mensaje que algo salio mal
            print('OH no, no sé que paso')

            # devolver error
            return 'Sigo esperando'


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el dia de la semana
def pedir_dia():

    # Crear variables con datos de hoy
    dia = datetime.date.today()

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()

    # Diccionario con nombres de dias
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sabado',
        6: 'Domingo'
    }
    hablar(f'Hoy es {calendario[dia_semana]}')


# Pedir hora
def pedir_hora():
    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minuto y {hora.second} segundos'

    # Decir la hora
    hablar(hora)


# Funcion saludo inicial
def saludo_inicial():
    # Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenas dias'
    else:
        momento = 'Buenos tardes'
    # Decir el saludo

    hablar(f'{momento}, soy Daniel, tu asistente personal. Por favor, dime lo que se te ofrezca')


# funcion central del sistema
def pedir_cosas():
    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop while
    while comenzar:
        # activar el micro y guardar el pedido en un strings
        pedido = transfomar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir google' in pedido:
            hablar('Con gusto, estoy abriendo google')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif ('qué hora es' or 'qué hora son') in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('buscar en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia ddice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            
            pywhatkit.sendwhatmsg('+51992984382','Cuantos años tienes prra',13, 2)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            print(accion)
            cartera = {
                'apple':'AAPL',
                'amazon':'AMZN',
                'meta':'META',
                'facebook':'FB',
                'ayuda':'MSFT'
            }
            try:
                sigla = cartera[accion]
                print(sigla)
                accion_buscada = yf.Ticker(sigla).info
                print(accion_buscada)
                precio_actual = accion_buscada['regularMarketPrice']
                print(precio_actual)
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la he encontrado')
                continue
        elif 'apágate' in pedido:
            hablar('okey, Me voy a descanzar, cualquier cosa me avisas')
            break

pedir_cosas()

# Visualizar los paquetes de voces que hay en tu maquina
# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#     print(voz)







