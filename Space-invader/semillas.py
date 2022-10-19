import pygame

#dimensiones de las semillas

class Semillas(pygame.sprite.Sprite):
    def __init__(self,screen, naveColibri):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("imagenes/nuez.png")
        #obtener las dimensiones de la imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = naveColibri.rect.centerx
        self.rect.top = naveColibri.rect.top
    def update(self):
        #genera movimiento y avanza 5 px hasta top
        self.rect.y -= 20



