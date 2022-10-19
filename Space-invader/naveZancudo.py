import pygame

FPS = 80
velocidad = pygame.time.Clock()
class NaveZancudo(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.attack_animation = False
        self.sprites = []

        self.sprites.append(pygame.image.load('imagenes/NaveZancudo__1.png'))
        self.sprites.append(pygame.image.load('imagenes/NaveZancudo__2.png'))
        #self.sprites.append(pygame.image.load('imagenes/NaveZancudo__3.png'))
        self.sprites.append(pygame.image.load('imagenes/NaveZancudo__4.png'))
        self.sprites.append(pygame.image.load('imagenes/NaveZancudo__5.png'))
        self.sprites.append(pygame.image.load('imagenes/NaveZancudo__6.png'))

        #load de la imagen y modificacion de la escala
        #self.image = pygame.image.load("./alien.bmp")
        #self.image = pygame.transform.scale(self.image,(110,90))
        self.sprite_actual = 0

        self.image = self.sprites[self.sprite_actual]

        #obtener las dimensiones de la imagen
        self.rect = self.sprites[self.sprite_actual].get_rect()
        #ubicacion
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #finura
        self.x = float(self.rect.x)



    def blitme(self):
        #graficar
        self.screen.blit(self.image,self.rect)
        self.sprite_actual += 1
        velocidad.tick(FPS)
        if self.sprite_actual >= len(self.sprites):
            self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]

    def update(self,cambioDeDireccion):
        #generar movimiento a la derecha de cada una de las navesZancudo
        self.rect.x += 1*cambioDeDireccion

    def validar_borde(self,cambioDeDrireccion):
        if self.rect.x >= 900:
            return True
        elif self.rect.x <= 0:
            return True

