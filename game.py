from player import Player


class Game:

    def __init__(self, players):
        players = [Player(i) for i in range(players)]
        board = []