import sys
from buttons import Button
import pygame

pygame.init()
res = [1200, 800]

screen = pygame.display.set_mode(res)

board = pygame.image.load("board.png")
boardrect = board.get_rect()
button_font = pygame.font.Font(None,30)

button1 = Button('ROLL DICE', (100, 50), (10, 10), 5, button_font)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
    screen.blit(board, (300,70))
    pygame.display.update()

    button1.draw(screen)
