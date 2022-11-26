import pygame
import random
# Inicializar la pantalla
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((1000,600))

# Titulo e Icono
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load('astronave.png')
img_escalada_jugador = pygame.transform.scale(img_jugador, (60, 60))
jugador_x = 470
jugador_y = 540
jugador_x_cambio = 0

# enemigo
img_enemigo = pygame.image.load('enemigo.png')
img_escalada_enemgio = pygame.transform.scale(img_enemigo, (60, 60))
enemigo_x = random.randint(0, 1000)
enemigo_y = random.randint(50, 450)
enemigo_x_cambio = 0


def jugador(x, y):
    pantalla.blit(img_escalada_jugador, (x, y))


def enemigo(x, y):
    pantalla.blit(img_escalada_enemgio, (x, y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((205, 144, 228))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    jugador_x += jugador_x_cambio
    # mantener dentro del borde
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 940:
        jugador_x = 940
    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)
    pygame.display.update()
