import pygame
from button import Button

pygame.init()
res = [1200, 800]
screen = pygame.display.set_mode(res)

button = Button(screen, (10, 10), (150, 100))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if button.action():
        print('c')
    button.draw()
    pygame.display.update()