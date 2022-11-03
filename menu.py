import sys
import pygame
from game import Game
from button import Button

class Menu:
    def __init__(self, screen):

        self.game = None
        self.buttons = [Button(screen, (500, 300), (180, 60), "NEW GAME"), Button(screen, (500, 400), (180, 60), "QUIT")]
        while not self.game:
            screen.fill((0, 100, 0))

            title_font_bottom = pygame.font.SysFont("title font", 100).render(str("MONOPOLY"), False, (0, 0, 0))
            screen.blit(title_font_bottom, (405, 55))
            title_font_top = pygame.font.SysFont("title font", 100).render(str("MONOPOLY"), False, (238, 59, 59))
            screen.blit(title_font_top, (400, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if self.buttons[0].action():
                self.game = Game(screen)

            if self.buttons[1].action():
                sys.exit()

            for button in self.buttons:
                button.draw()

            pygame.display.update()
