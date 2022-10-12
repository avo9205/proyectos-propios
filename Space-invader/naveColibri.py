''' modelado de la nave colibri choneta '''
import pygame


class NaveColibri():
    def __init__(self,screen):
        self.screen = screen

        self.imagen = pygame.image.load("./nave.bmp")
        self.imagen = pygame.transform.scale(self.imagen,(150,110))
        self.rect = self.imagen.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom =self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.imagen, self.rect)