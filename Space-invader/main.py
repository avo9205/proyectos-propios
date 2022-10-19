import pygame, sys
from naveColibri import NaveColibri
from fondo import Fondo
import funciones as fun
from semillas import Semillas
from naveZancudo import NaveZancudo



''' Imagen icono ventana  '''
imagenIcono = pygame.image.load("imagenes/secuestro.png")


FPS = 8

def run_game():
    pygame.init()
    '''temporizador'''
    velocidad = pygame.time.Clock()

    ''' creación de la pantalla, con las dimensiones propuestas en size '''
    windth, heigth = 900, 600
    screen = pygame.display.set_mode((windth, heigth))

    '''Caption -> nombre ventana'''
    pygame.display.set_caption("El ataque de los colibrís salvajes de Adolfo")
    pygame.display.set_icon(imagenIcono)

    ''' creando un objeto de nave colibri con los parametros del tamaño
     de la pantala'''
    naveColibri = NaveColibri(screen)

    '''creacion del objeto naveZancudo'''
    naveZancudo = NaveZancudo(screen)


    '''es un bucle que se activa solo si hay un evento generado por el el usuario
    ya sea el presionar una tecla o un click del mouse, la intencion es 
    gestionar las actualizacion'''

    '''Creacion de los sprites'''
    moving_sprites = pygame.sprite.Group()
    fondo_moving = Fondo()
    moving_sprites.add(fondo_moving)

    '''crecacion del grupo de semillas, que almacenara los sprites'''
    lista_semillas = pygame.sprite.Group()

    '''flota de naves'''
    flotaDeNaves = pygame.sprite.Group()
    fun.crear_flota(screen, flotaDeNaves)

    '''cambio de direccion de las navesZancudo'''
    cambioDeDireccion = 1

    while True:
        fun.check_eventos(naveColibri,screen,lista_semillas)
        naveColibri.update()



        fun.eliminar_semillas(lista_semillas)

        fun.actualizaciones_pantalla(moving_sprites ,screen ,FPS ,velocidad ,
                                     naveColibri,lista_semillas,naveZancudo,
                                     flotaDeNaves,cambioDeDireccion)

        fun.actualizar_flota(flotaDeNaves,cambioDeDireccion)
        fun.generar_movimiento_naves(flotaDeNaves)

run_game()
