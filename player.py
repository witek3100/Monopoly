import pygame
from game import Game

class Player:

    def __init__(self, screen, num):
        self.screen = screen
        self.number = num
        self.board_position = 0
        self.screen_position = Game.board_fields_data[self.board_position]
        self.money = 1500
        self.own_districts = []

    def draw(self):
        pygame.draw.rect(self.screen, (255,185,15), (self.screen_position, (15, 40)))

    def move(self, pos):
        self.board_position += pos
        self.screen_position = Game.board_fields_data[self.board_position]
