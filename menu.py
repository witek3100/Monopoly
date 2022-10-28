import sys
import pygame
from game import Game
from button import Button

class Menu:
    def __init__(self, screen):

        self.game = None
        while not self.game:
            screen.fill((0, 100, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            button = Button(screen, (500, 300), (180, 60), "NEW GAME")
            if button.action():
                self.game = Game(screen)
            button.draw()
            pygame.display.update()
