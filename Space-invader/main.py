import pygame, sys
from naveColibri import NaveColibri
from fondo import Fondo




''' Imagen icono ventana  '''
imagenIcono = pygame.image.load("./secuestro.png")


FPS = 8

def run_game():
    pygame.init()
    '''temporizador'''
    velocidad = pygame.time.Clock()

    ''' creación de la pantalla, con las dimensiones propuestas en size '''
    windth, heigth = 900, 600
    x,y = 0,0
    screen = pygame.display.set_mode((windth, heigth))

    '''Caption -> nombre ventana'''
    pygame.display.set_caption("El ataque de los colibrís salvajes de Adolfo")
    pygame.display.set_icon(imagenIcono)

    ''' creando un objeto de nave colibri con los parametros del tamaño
     de la pantala'''
    naveColibri = NaveColibri(screen)
    '''es un bucle que se activa solo si hay un evento generado por el el usuario
    ya sea el presionar una tecla o un click del mouse, la intencion es 
    gestionar las actualizacion'''

    '''Creacion de los sprites'''
    moving_sprites = pygame.sprite.Group()
    fondo_moving = Fondo()
    moving_sprites.add(fondo_moving)

    while True:

        for eventos in pygame.event.get():
            # Es lo que especifica la velocidad del bucle de juego

            """si el usurio presiona cerrar entonces sys cierra el programa"""
            if eventos.type == pygame.QUIT:
                sys.exit()
        moving_sprites.draw(screen)
        moving_sprites.update()
        velocidad.tick(FPS)

        naveColibri.blitme()
        pygame.display.update()
run_game()
