import random

from player import Player
from button import Button
from window import Window
import pygame

class BoardField:

    def __init__(self, screen, name, pos, type):
        self.name = name
        self.position = pos
        self.screen = screen
        self.image = pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/district.xcf")
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
        if self.type == "chance":
            print("chance")
        if self.type == "prize":
            player.money += 500
        if self.type == "jail":
            player.lock_in_prison()

class DistrictField(BoardField):

    def __init__(self, screen, name, pos, type):
        super().__init__(screen, name, pos, type)
        self.owner = None
        self.price = 0
        self.house_price = 0
        self.houses = 0
        self.fees = []
        self.color = random.choice(['red','blue','green','yellow'])
        self.image = pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/"+self.color+"_district.xcf")

    def action(self, player):
        if self.owner == None:
            buy_win = Window(self.screen, [str(self.name) + " has no owner",  "Would you like to buy it for " + str(self.price) + "?"])
            if buy_win.action():
                self.buy_district(player)
        else:
            pass

    def buy_district(self, player):
        self.owner = player
        if self.color in player.own_districts:
            player.own_districts.get(self.color).append(self)
        else:
            player.own_districts[self.color] = [self]
        player.money -= self.price
        print(player.own_districts)
        return
