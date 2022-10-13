import pygame
import sys

def check_eventos(naveColibri):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Nave Colibrí
            elif event.type == pygame.KEYDOWN:
                #tecla flecha derecha
                if event.key == pygame.K_RIGHT:
                    naveColibri.mov_derecha =True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    naveColibri.mov_derecha = False
            pygame.display.update()


def actualizaciones_pantalla(moving_sprites,screen,FPS,velocidad, naveColibri):
    moving_sprites.draw(screen)
    # metodo que llama la funcion que recorre los fotogramas
    moving_sprites.update()
    # velocidad de mov de los fotogramas
    velocidad.tick(FPS)
    # creacion de la nave
    naveColibri.blitme()
    # actualiza la pantalla
    pygame.display.update()
