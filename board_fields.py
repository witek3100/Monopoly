from player import Player
from button import Button
from window import Window
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
        self.color = "red"

    def action(self, player):
        if self.owner == None:
            buy_win = Window(self.screen, [str(self.name) + " has no owner",  "Would you like to buy it for " + str(self.price) + "?"])
            if buy_win.action():
                self.buy_district(player)
        else:
            pass

    def buy_district(self, player):
        self.owner = player
        for i in player.own_districts:
            if i[0].color == self.color:
                i.append(self)
            player.own_districts.append([[self]])

        player.money -= self.price
        return
