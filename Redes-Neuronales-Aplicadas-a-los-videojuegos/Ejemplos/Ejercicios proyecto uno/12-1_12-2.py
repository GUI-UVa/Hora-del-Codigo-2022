
import sys
import pygame

from Config import Setting 

class Juego:

    def __init__(self):
        pygame.init()
        self.config = Setting()
        self.screen = pygame.display.set_mode(self.config.screen_dim)
        self.gregori = self.config.Gregori(self)
        pygame.display.set_caption('12_1')
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.config.bg_color)
            self.config.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    jg = Juego()
    jg.run_game()

