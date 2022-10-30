from player import Player
from button import Button
import pygame

class BoardField:

    def __init__(self, screen, name, pos):
        self.name = name
        self.position = pos
        self.screen = screen
        self.image = pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/district.jpeg")
        self.area = pygame.Rect(pos, (100, 100))

    def show_information(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.area.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        return action

    def action(self, player):
        player.money -= 100


class DistrictField(BoardField):

    def __init__(self, screen, name, pos):
        super().__init__(screen, name, pos)
        self.image = None

