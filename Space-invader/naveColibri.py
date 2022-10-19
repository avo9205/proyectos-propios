''' modelado de la nave colibri choneta '''
import pygame

FPS = 80
velocidad = pygame.time.Clock()

class NaveColibri(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('imagenes/NaveColibri.png'))
        self.sprites.append(pygame.image.load('imagenes/NaveColibri2.png'))
        self.sprites.append(pygame.image.load('imagenes/NaveColibri3.png'))
        self.sprites.append(pygame.image.load('imagenes/NaveColibri4.png'))

        self.sprite_actual = 0

        self.image = self.sprites[self.sprite_actual]

        #self.imagen = pygame.image.load("./nave.bmp")
        #self.imagen = pygame.transform.scale(self.imagen,(200,150))

        self.rect = self.sprites[self.sprite_actual].get_rect()

        self.screen_rect = screen.get_rect()

        self.rect.centerx = float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        self.mov_derecha = False
        self.mov_izquierda = False
        self.mov_arriba = False
        self.mov_abajo = False

    def update(self):

        # si el movimiento es verdadero y esta en los limistes de screen
        if self.mov_derecha and self.rect.right <= self.screen_rect.right + 15:
            velocidad.tick(FPS)
            self.rect.centerx += 50

        elif self.mov_izquierda and self.rect.left + 15 >= self.screen_rect.left:
            velocidad.tick(FPS)
            self.rect.centerx -= 50
        elif self.mov_arriba and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 50

        elif self.mov_abajo and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 20


    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.sprite_actual += 1
        velocidad.tick(80)
        if self.sprite_actual >= len(self.sprites):
            self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]
