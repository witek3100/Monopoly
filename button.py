import time

import pygame

pygame.font.init()

class Button:

    def __init__(self, screen, pos, size, text):
        #main vars
        self.screen = screen
        self.position = pos
        self.size = size
        self.top_rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.bottom_rect = pygame.Rect(self.position[0] + 3, self.position[1] + 10, self.size[0], self.size[1])
        self.pressed = False

        #colors
        self.__top_rect_normal_color = (24,116,205)
        self.__top_rect_hovered_color = (30,144,255)
        self.__bottom_rect_normal_color = (16,78,139)
        self.__bottom_rect_hovered_color = (28,134,238)

        self.__top_rect_color = self.__top_rect_normal_color
        self.__bottom_rect_color = self.__bottom_rect_normal_color

        #text
        self.__text_font = pygame.font.SysFont(str(text) + "font", 30)
        self.__text = self.__text_font.render(text, False, (0, 0, 0))

    def draw(self):

        pygame.draw.circle(self.screen, self.__bottom_rect_color, self.bottom_rect.bottomleft, 10)
        pygame.draw.circle(self.screen, self.__bottom_rect_color, self.bottom_rect.bottomright, 10)
        pygame.draw.circle(self.screen, self.__bottom_rect_color, self.bottom_rect.topright, 10)
        pygame.draw.rect(self.screen, self.__bottom_rect_color, ((self.bottom_rect.topleft[0] - 10, self.bottom_rect.topleft[1]), (self.bottom_rect.size[0] + 20, self.bottom_rect.size[1])))
        pygame.draw.rect(self.screen, self.__bottom_rect_color, ((self.bottom_rect.topleft[0], self.bottom_rect.topleft[1] - 10), (self.bottom_rect.size[0], self.bottom_rect.size[1] + 20)))

        pygame.draw.circle(self.screen, self.__top_rect_color, self.top_rect.bottomleft, 10)
        pygame.draw.circle(self.screen, self.__top_rect_color, self.top_rect.bottomright, 10)
        pygame.draw.circle(self.screen, self.__top_rect_color, self.top_rect.topleft, 10)
        pygame.draw.circle(self.screen, self.__top_rect_color, self.top_rect.topright, 10)
        pygame.draw.rect(self.screen, self.__top_rect_color, ((self.top_rect.topleft[0] - 10, self.top_rect.topleft[1]), (self.top_rect.size[0] + 20, self.top_rect.size[1])))
        pygame.draw.rect(self.screen, self.__top_rect_color, ((self.top_rect.topleft[0], self.top_rect.topleft[1] - 10), (self.top_rect.size[0], self.top_rect.size[1] + 20)))

        self.screen.blit(self.__text, (self.position))

    def action(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(pos):
            self.__top_rect_color = self.__top_rect_hovered_color
            self.__bottom_rect_color = self.__bottom_rect_hovered_color
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                action = True
        else:
            self.__top_rect_color = self.__top_rect_normal_color
            self.__bottom_rect_color = self.__bottom_rect_normal_color
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False

        return action