import pygame


class Player:

    def __init__(self, screen, num):
        self.screen = screen
        self.number = num
        self.board_position = 0

        self.money = 1500
        self.own_districts = []

    def draw(self):
        pygame.draw.rect(self.screen, (255,185,15), ((0 + self.board_position, 400), (15, 40)))

    def move(self, pos):
        self.board_position += pos

