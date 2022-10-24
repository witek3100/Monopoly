from game import Game
import pygame

pygame.init()
res = [1200, 800]
screen = pygame.display.set_mode(res)

game = Game(1, screen)
game.game_loop()
