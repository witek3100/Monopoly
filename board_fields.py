import random

from player import Player
from button import Button
from window import Window, Buy_district_window
import pygame

class BoardField:

    def __init__(self, game, name, pos, type):
        self.name = name
        self.position = pos
        self.game = game
        self.image = pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/district.xcf")
        self.area = pygame.Rect(self.position)
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

    def __init__(self, screen, name, pos, type, color):
        super().__init__(screen, name, pos, type)
        self.owner = None
        self.price = 0
        self.house_price = 50
        self.houses = 0
        self.fees = []
        self.color = color
        if self.color in ['Grecee', 'Switzerland']:
            self.color_dis_am = 2
        else:
            self.color_dis_am = 3
        self.image = pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/"+self.color+"_district.xcf")

    def action(self, player):
        if self.owner == None:
            buy_win = Buy_district_window(self.game.screen, [str(self.name) + " has no owner",  "Would you like to buy it for " + str(self.price) + "?"])
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
        return [pygame.Rect(self.position[0][0], self.position[0][1], self.position[1][0], self.position[1][1]), (self.position[1][0], self.position[1][1])]

    def buy_house(self):
        self.houses += 1
        self.owner.money -= self.house_price

    def pawn(self):
        pass
