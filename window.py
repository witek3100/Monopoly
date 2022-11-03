import time

from button import Button
import pygame
import sys

class Window:

    def __init__(self, screen, text):
        self.screen = screen
        self.text = text
        self.color = (139,69,19)
        self.win_rect = pygame.Rect(390, 240, 380, 205)
        self.buttons = [Button(self.screen, (self.win_rect.bottomleft[0] + 20, self.win_rect.bottomleft[1] - 80), (100, 60), "YES"), Button(self.screen, (self.win_rect.bottomright[0] - 120, self.win_rect.bottomright[1] - 80), (100, 60), "NO")]

    def action(self) -> bool:

        pygame.draw.circle(self.screen, self.color, self.win_rect.bottomleft, 20)
        pygame.draw.circle(self.screen, self.color, self.win_rect.bottomright, 20)
        pygame.draw.circle(self.screen, self.color, self.win_rect.topright, 20)
        pygame.draw.circle(self.screen, self.color, self.win_rect.topleft, 20)
        pygame.draw.rect(self.screen, self.color, ((self.win_rect.topleft[0] - 20, self.win_rect.topleft[1]), (self.win_rect.size[0] + 40, self.win_rect.size[1])))
        pygame.draw.rect(self.screen, self.color, ((self.win_rect.topleft[0], self.win_rect.topleft[1] - 20), (self.win_rect.size[0], self.win_rect.size[1] + 40)))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            text = pygame.font.SysFont("buy font", 30).render(self.text[0], False, (0, 0, 0))
            self.screen.blit(text, (self.win_rect.topleft[0] + 20, self.win_rect.topleft[1] + 20))

            text = pygame.font.SysFont("buy font", 30).render(self.text[1], False, (0, 0, 0))
            self.screen.blit(text, (self.win_rect.topleft[0] + 20, self.win_rect.topleft[1] + 55))

            for button in self.buttons:
                button.draw()
            if self.buttons[0].action():
                return True
            if self.buttons[1].action():
                return False
            pygame.display.update()
