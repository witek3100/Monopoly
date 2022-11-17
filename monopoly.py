import pygame
from menu import Menu

pygame.init()
res = [1500, 900]
screen = pygame.display.set_mode(res)
pygame.display.set_caption("MONOPOLY")

while True:
    game = Menu(screen).game
    game.game_loop()



