import pygame
import random
import math
from pygame import mixer  # Para sonido
# Inicializar la pantalla
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((1000,600))

# Titulo e Icono
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')
img_fondo_escalada = pygame.transform.scale(fondo,(1000, 600))

# agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.1)  # Volumen
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load('astronave.png')
img_escalada_jugador = pygame.transform.scale(img_jugador, (60, 60))
jugador_x = 470
jugador_y = 520
jugador_x_cambio = 0

# enemigo
img_enemigo = []
img_escalada_enemgio = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigo = 8

for e in range(cantidad_enemigo):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    img_escalada_enemgio.append(pygame.transform.scale(img_enemigo[e-1], (60, 60)))
    enemigo_x.append(random.randint(0, 1000))
    enemigo_y.append(random.randint(50, 250))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# bala
img_bala = pygame.image.load('bala.png')
img_escalada_bala = pygame.transform.scale(img_bala, (30, 30))
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 60)


def texto_final():
    mi_fuente_final = fuente_final.render('Juego Terminado', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final,(250, 250))


def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    pantalla.blit(texto, (x, y))


def jugador(x, y):
    pantalla.blit(img_escalada_jugador, (x, y))


def enemigo(x, y, ene):
    pantalla.blit(img_escalada_enemgio[ene], (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_escalada_bala, (x + 16, y + 10))


# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2-x_1, 2) + math.pow(y_2-y_1, 2))
    if distancia < 20:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    # pantalla.fill((205, 144, 228))
    # Imagen de fondo
    pantalla.blit(img_fondo_escalada,(0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.8
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.8
            if evento.key == pygame.K_SPACE:

                if not bala_visible:
                    bala_x = jugador_x
                    mixer.Sound('disparo.mp3').play()
                    disparar_bala(bala_x, bala_y)
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar ubicacion del jugador
    jugador_x += jugador_x_cambio

    # mantener dentro del borde al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 940:
        jugador_x = 940

    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigo):

        # fin del juego
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigo):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
        # mantener dentro del borde al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 940:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            mixer.Sound('Golpe.mp3').play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 1000)
            enemigo_y[e] = random.randint(10, 100)

        enemigo(enemigo_x[e], enemigo_y[e], e)
    # movimiento bala
    if bala_y <= -30:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)
    # Actualiza
    pygame.display.update()


