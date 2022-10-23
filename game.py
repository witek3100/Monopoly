from player import Player
from buttons import Button
import random


class Game:

    def __init__(self, players):
        self.players = [Player(i) for i in range(players)]
        self.board = []

    def player_turn(self, player):
        c = random.randint(1,12)