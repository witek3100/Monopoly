from player import Player
from button import Button

class BoardField:

    def __init__(self, screen, name, pos):
        self.name = name
        self.position = pos
        self.screen = screen
        self.button = Button(self.screen, pos, (40, 100), "")

    def action(self, player):
        player.money += 10

class DistrictField(BoardField):
    pass