import sys

import pygame
from button import Button


class Game:

    def __init__(self, screen):
        self.screen = screen

    def game_loop(self):
        board = pygame.image.load("board.xcf")
        button = Button(self.screen, (10, 10), (140, 70), "DICE")
        run = True
        while run:
            self.screen.fill((0, 100, 0))
            self.screen.blit(board, (300, 70))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if button.action():
                print('c')
            button.draw()
            pygame.display.update()