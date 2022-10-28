import pygame


class Player:

    def __init__(self, screen):
        self.screen = screen
        self.number = 1
        self.position = 0
        self.money = 1500
        self.own_districts = []

    def draw(self):
        pygame.draw.rect(self.screen, )