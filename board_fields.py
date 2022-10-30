from player import Player
from button import Button
import pygame

class BoardField:

    def __init__(self, screen, name, pos, type):
        self.name = name
        self.position = pos
        self.screen = screen
        self.image = pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/district.jpeg")
        self.area = pygame.Rect(pos, (100, 100))
        self.type = type

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
            print("fee")
        if self.type == "chance":
            print("chance")
        if self.type == "prize":
            player.money += 500
            print("prize")
        if self.type == "jail":
            player.lock_in_prison()

class DistrictField(BoardField):

    def __init__(self, screen, name, pos, type):
        super().__init__(screen, name, pos, type)
        self.owner = None

    def action(self, player):
        if self.owner == None:
            print("DF")
        else:
            pass