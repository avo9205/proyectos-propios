import pygame

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('imagenes/Space_invader_000.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_001.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_002.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_003.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_004.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_005.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_006.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_007.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_008.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_009.jpg'))
        self.sprites.append(pygame.image.load('imagenes/Space_invader_010.jpg'))
        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]

        self.rect = self.image.get_rect()



    def update(self):
        self.sprite_actual += 1
        if self.sprite_actual >= len(self.sprites):
            self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]