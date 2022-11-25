import sys
import pygame

pygame.init()
dim = (1400, 800)
screen = pygame.display.set_mode(dim)
x = 300
y = dim[1]/2
rect = (25, 75)
bg_color = (230, 230, 230)
rect_color = (0, 0, 0)
vel = 1
screen_rect = screen.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()

    if x == dim[0] - vel:
        x = 0 + vel
    elif x == 0 + vel:
        x = dim[0] - vel

    if y == dim[1] - vel:
        y = 0 + vel
    elif y == 0 + vel:
        y = dim[1] - vel

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill(bg_color)
    rect_black = pygame.draw.rect(screen, rect_color, (x, y, rect[0], rect[1]))
    
    if rect_black not in screen_rect:
        x = dim[0]/2 
        y = dim[1]/2
    pygame.display.update()  

 