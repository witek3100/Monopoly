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
        self.type = "fee"

    def show_information(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.area.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        return action

    def action(self, player):
        if self.type == "fee":
            player.money -= 200
        if self.type == "chance":
            pass
        if self.type == "prize":
            player.money += 500


class DistrictField(BoardField):

    def __init__(self, screen, name, pos):
        super().__init__(screen, name, pos)
        self.ownner = None
