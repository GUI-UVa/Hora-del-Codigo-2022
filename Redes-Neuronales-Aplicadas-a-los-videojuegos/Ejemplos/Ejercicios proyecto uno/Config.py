import pygame

class Setting:

    def __init__(self):
        self.screen_dim = (1024, 600)
        self.bg_color = (135, 206, 235)
    
    def Gregori(self, juego):
        self.screen = juego.screen
        self.screen_rect = juego.screen.get_rect()

        self.image = pygame.image.load('Ejercicios proyecto uno\Greg.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)