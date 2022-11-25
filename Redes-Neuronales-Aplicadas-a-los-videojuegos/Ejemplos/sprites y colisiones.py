from sys import exit                    
from random import randint, choice

import pygame
from pygame import sprite

win_size = (1400,800)
#Colisiona con todos los enemigos para 'ganar'
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(win_size)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Colisiones')

        self.enemies = pygame.sprite.Group()
        self.player0 = pygame.sprite.GroupSingle() #Grupo de un solo sprite

        self.player = Player(self)

    def run_game(self):
        while True:
            self.check_events()
            self.update_player()
            self.update_enemies()
            self.check_colisions()
            self.update_screen()
              
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True 

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False 

    def update_screen(self):
        self.screen.fill((230, 230, 230))
        self.player0.draw(self.screen)      #Dibuja los sprites contenidos en el grupo
        self.enemies.draw(self.screen)      
        pygame.display.flip()

    def update_player(self):
        if len(self.player0.sprites()) == 0:
            self.create_player()

        self.player0.update()               #Llama al método update() contenido en cada miembro del sprite (en este caso solo 1)
        
    def create_player(self):
        self.player0.add(self.player)       #Se añade la instancia con la que trabajamos de la clase Player al Gropusingle de sprite player0
    
    def update_enemies(self):
        if len(self.enemies.sprites()) == 0: #Si la lista devuelta del grupo de Sprites está vacía generará otros 10 enemigos
            for n in range(0, 10):
                self.create_enemie()

        self.enemies.update()

    def create_enemie(self):
        enemy = Enemy(self)
        self.enemies.add(enemy)
    
    def check_colisions(self):
        pygame.sprite.groupcollide(self.player0, self.enemies, False, True, collided = None)    #Detecta la colisión y los True/False 'matán' o no a los miebros colisionados 
        #groupcollide devuelve un diccionario de los sprites que han colisionado del primer grupo ,y en cada uno de ellos se asocia una lista de sprites del segundo grupo con los que ha colisionado.


class Player(sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp') #Se carga la imagen de la nave
        self.rect = self.image.get_rect()#Del tamaño de la imagen se saca un rect y se comporta como tal.

        self.rect.x = self.screen_rect.centerx #Posición inicial
        self.rect.y = 700
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.vel = 1    

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.vel
        if self.moving_left and self.rect.left > 0:
            self.x -= self.vel
        if self.moving_up and self.rect.top > 0:
            self.y -= self.vel
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.vel
        
        self.rect.x = self.x
        self.rect.y = self.y
        


class Enemy(sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/greg.bmp')
        self.rect = self.image.get_rect()

        vel_ch = [1, -1]
        self.vel = [choice(vel_ch) , choice(vel_ch) ] #Velocidad en [x, y]
        

        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery
        self.x = float(self.rect.x) 
        self.y = float(self.rect.y)
        
    def update(self):                              
        if self.rect.right == self.screen_rect.right:  #Comprobar choques con bordes de pantalla en x
            self.vel[0] =- self.vel[0]
            self.vel[1] =+ randint(-1 , 1) 
        elif self.rect.left == 0:
            self.vel[0] =- self.vel[0]
            self.vel[1] =+ randint(-1 , 1)
        elif self.rect.top == 0:                       #Comprobar choques con bordes de pantalla en y
            self.vel[1] =- self.vel[1]
            self.vel[0] =+ randint(-1 , 1)  
        elif self.rect.bottom == self.screen_rect.bottom:
            self.vel[1] =- self.vel[1]
            self.vel[0] =+ randint(-1 , 1)

        if self.rect not in self.screen_rect: #Si se salen de la pantalla por error reaparecen en el centro.
            self.x = self.screen_rect.centerx
            self.y = self.screen_rect.centery
            
        self.x += self.vel[0] #Velocidad en x
        self.y += self.vel[1] #Velocidad en y

        self.rect.x = self.x
        self.rect.y = self.y
    
if __name__ == '__main__':
    G = Game()
    G.run_game()


