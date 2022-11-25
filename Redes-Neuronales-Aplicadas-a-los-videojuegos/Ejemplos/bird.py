import pygame
from pygame.locals import *
import sys
from random import randint

pygame.init()

vec = pygame.math.Vector2
HEIGHT = 450
WIDTH = 600
ACC = 2
FRIC = -0.12
FPS = 60
YELLOW = (255, 255, 40)
GREEN  = (128, 255, 40)
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Player():
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(vec(30, 30))
        self.surf.fill(YELLOW)
        self.rect = self.surf.get_rect()
        self.pos = vec((75, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.midbottom = self.pos

    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.acc.y = -ACC*0.9
        else:
            self.acc.y = ACC/5
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.y > HE  IGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        self.rect.midbottom = self.pos

class platform():
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((50, HEIGHT))
        self.surf.fill(YELLOW)
        self.rect = self.surf.get_rect()
        self.pos = pos
        self.rect.midbottom = self.pos
    def scroll(self, player, rand):
        self.pos.x -= 1
        if self.rect.colliderect(player):
            pygame.quit()
            sys.exit()
        self.rect.midbottom = self.pos

class flappyBird:
    def __init__(self):
        self.player = Player()
        rand = randint(25, HEIGHT-175)
        self.pipes = []
        self.pipes.append(platform(vec(WIDTH, rand)))
        self.pipes.append(platform(vec(WIDTH, rand + 150 + HEIGHT)))
        rand = randint(25, HEIGHT-175)
        self.pipes.append(platform(vec(WIDTH + 300, rand)))
        self.pipes.append(platform(vec(WIDTH + 300, rand + 150 + HEIGHT)))
        self.score = 0
        self.pipeState = True

    def update(self):
        self.player.move()
        for pipe in self.pipes:
            pipe.scroll(self.player.rect, randint(25, HEIGHT-175))
        if self.pipes[0].pos.x < 25 and self.pipeState == True:
            self.pipeState = False
            self.score += 1
        if self.pipes[0].pos.x < -50:
            self.pipeState = True
            self.pipes.pop(0)
            self.pipes.pop(0)
            rand = randint(25, HEIGHT-175)
            self.pipes.append(platform(vec(WIDTH, rand)))
            self.pipes.append(platform(vec(WIDTH, rand + 150 + HEIGHT)))

    def draw(self):
        displaysurface.fill((255,0,0))
        displaysurface.blit(self.player.surf, self.player.rect)
        for pipe in self.pipes:
            displaysurface.blit(pipe.surf, pipe.rect)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.score), True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (25, 25)
        displaysurface.blit(text, textRect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()
            pygame.display.update()
            FramePerSec.tick(FPS)

if __name__ == "__main__":
    game = flappyBird()
    game.run()