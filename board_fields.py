from player import Player


class BoardField:

    def __init__(self, name, pos):
        self.name = name
        self.position = pos

    def action(self, player):
        player.money += 10

class DistrictField(BoardField):
    pass