import pygame
import boardFieldsData
import random

class Player:

    def __init__(self, screen, num):
        self.screen = screen
        self.number = num
        self.position = 0

        self.money = 1500
        self.own_districts = []

    def draw(self):
        pygame.draw.rect(self.screen, (255,185,15), (boardFieldsData.fields_data[self.position][1], (20, 20)))
        pass

    def move(self):
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        self.position = (self.position + first_dice) % 40
