import pygame
import sys

from naveZancudo import NaveZancudo
from semillas import Semillas

#---------------Metodos de Semillas---------------------

def lanzar_semillas(naveColibri,screen,lista_semillas):
    # si la lista de sprite es menor 10 permitira generar semillas
    if len(lista_semillas) < 10:
        nueva_semilla = Semillas(screen, naveColibri)
        # nueva_semilla.rect.x = naveColibri.rect.centerx
        # semillas del Groud
        lista_semillas.add(nueva_semilla)
# ------------------ Eliminar semillas -------------------
def eliminar_semillas(lista_semillas):
    for semilla in lista_semillas.copy():
        if semilla.rect.bottom <= 0:
            lista_semillas.remove(semilla)

#---------------Metodos presionar teclas ----------------
def KeyDown (eventos,naveColibri,screen,lista_semillas):
    # movimiento según las fechas
    if eventos.key == pygame.K_RIGHT:
        naveColibri.mov_derecha = True
    elif eventos.key == pygame.K_LEFT:
        naveColibri.mov_izquierda = True
    elif eventos.key == pygame.K_UP:
        naveColibri.mov_arriba = True
    elif eventos.key == pygame.K_DOWN:
        naveColibri.mov_abajo = True

    # objeto de semilllas que llama los parametros de la pantlla y la nave
    elif eventos.key == pygame.K_SPACE or eventos.key == pygame:
        lanzar_semillas(naveColibri,screen,lista_semillas)

    elif eventos.key == pygame.K_q:
        sys.exit()

#----------Metodos al soltar las fechas teclas -----------

def keyUp(eventos, naveColibri):
    if eventos.key == pygame.K_RIGHT:
        naveColibri.mov_derecha = False
    elif eventos.key == pygame.K_LEFT:
        naveColibri.mov_izquierda = False
    elif eventos.key == pygame.K_UP:
        naveColibri.mov_arriba = False
    elif eventos.key == pygame.K_DOWN:
        naveColibri.mov_abajo = False

#----------control de eventos ---------------------------
def check_eventos(naveColibri,screen,lista_semillas):
    for eventos in pygame.event.get():
        # Es lo que especifica la velocidad del bucle de juego
        """si el usurio presiona cerrar entonces sys cierra el programa"""
        if eventos.type == pygame.QUIT:
            sys.exit()
        # Nave Colibrí- derecha
        elif eventos.type == pygame.KEYDOWN:
            #eventos de presion de teclas
            KeyDown(eventos,naveColibri,screen,lista_semillas)

        elif eventos.type == pygame.KEYUP:
            # eventos de no presion de teclas
            keyUp(eventos, naveColibri)

#-----Metodos get del numero de naves que puede entrar horizoltalmente -------------------------------------------------
def get_numero_de_nave_x(screen):
    # objeto de  referencia
    naveZancudo = NaveZancudo(screen)
    # se obtiene la dimension x del objeto
    naveZancudo_ancho = naveZancudo.rect.width
    # se dejara dos espacio libres de la pantalla
    espacio_disponible = 900 - naveZancudo_ancho
    # el numero de naves es la razon entre el espacio libre y el tamaño de las naves
    numero_naves_x = int(espacio_disponible / (naveZancudo_ancho))
    return numero_naves_x

def get_numero_de_nave_y(screen):
    naveZancudo = NaveZancudo(screen)
    espacio_disponible_y = 600 - 3*naveZancudo.rect.height
    numero_naves_y = espacio_disponible_y/naveZancudo.rect.height
    return numero_naves_y

#----------ingresa el numero de naves que puede haber, y se añaden a un lista de spiter -----------
def crear_lista_de_naves(screen,flotaDeNaves,numero_columnas,numero_filas):
    # objeto de  referencia
    naveZancudo = NaveZancudo(screen)
    # define el ancho y alto de la nave
    naveZancudo_ancho = naveZancudo.rect.width
    naveZancudo_alto = naveZancudo.rect.height

    #ubicacion en x,y, demodo que la nueva nave este al doble de la anterior
    naveZancudo.x = naveZancudo_ancho + naveZancudo_ancho*numero_columnas
    naveZancudo.y = naveZancudo_alto + naveZancudo_alto*numero_filas

    #se obtiene la posicion de x de la nave
    naveZancudo.rect.x = naveZancudo.x - 110
    naveZancudo.rect.y = naveZancudo.y - 75

    naveZancudo.blitme()
    flotaDeNaves.add(naveZancudo)

# ---------------------- Flota de naves -----------------------------#
def crear_flota(screen, flotaDeNaves):
    #de la funcion se obtiene el numero de naves que puede generar
    numero_naves_x = get_numero_de_nave_x(screen)
    numero_naves_y = int(get_numero_de_nave_y(screen))
    for numero_columnas in range(0,numero_naves_x,1):
        for numero_filas in range(0, numero_naves_y, 1):
            # objeto de  referencia
            crear_lista_de_naves(screen, flotaDeNaves,numero_columnas,numero_filas)

def generar_movimiento_naves(flotaDeNaves):

    for naves in (flotaDeNaves.sprites()):
        return naves.blitme()



#--------------------- validacion de los bordes ------------------------------------------------------------------------
'''def esta_en_borde(flotaDeNaves):
    for nave in flotaDeNaves.sprites():
        #si la nave esta en un borde, se genera verdadero
        if nave.rect.x >= 900:
            #si es asi chace un cambio de sentido
            nave.rect.x = -1
            cambio(flotaDeNaves)
        elif nave.rect.x <= 0:
            nave.rect.x = 1
            cambio(flotaDeNaves)
            break'''

'''def cambio(flotaDeNaves):
    # si la nave esta cambiando de sentido entonces va a desender
    # y sea aplicara un cambio de sentido en x, factorizando un menos
    for nave in flotaDeNaves.sprites():
        nave.rect.y += 1'''

#-------------------Actualizar flotas --------------------------------
def actualizar_flota(flotaDeNaves,cambioDeDrireccion):

    #esta_en_borde(flotaDeNaves,)
    for nave in flotaDeNaves.sprites():
        # si la nave esta en un borde, se genera verdadero
        if nave.rect.x >= 900 - nave.rect.width:
            # si es asi chace un cambio de sentido
            cambioDeDrireccion = -1
            pass
        elif nave.rect.x <= 0:
            cambioDeDrireccion = 1
        #flotaDeNaves.update(cambioDeDrireccion)

def actualizaciones_pantalla(moving_sprites,screen,FPS,velocidad,
                             naveColibri,lista_semillas, naveZancudo,
                             flotaDeNaves,cambioDeDireccion):
    '''for semilla in semillas.sprites():
        semilla.dibujar()'''

    moving_sprites.draw(screen)
    lista_semillas.draw(screen)
    flotaDeNaves.draw(screen)

    #flotaDeNaves.update(cambioDeDireccion)
    # metodo que llama la funcion que recorre los fotogramas
    moving_sprites.update()
    # metodo de llama la listos de semillas
    lista_semillas.update()




    # velocidad de mov de los fotogramas
    velocidad.tick(FPS)
    # creacion de la nave
    naveColibri.blitme()
    # creacion de la nave alien
    #naveZancudo.blitme()



    # actualiza la pantalla
    pygame.display.update()