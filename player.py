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

    def move(self) -> pygame.image:
        first_dice = random.randint(1,6)
        pygame.display.update()
        second_dice = random.randint(1,6)
        self.position = (self.position + first_dice) % 40
        if first_dice == 1:
            return pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice1.xcf")
        if first_dice == 2:
            return pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice2.xcf")
        if first_dice == 3:
            return pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice3.xcf")
        if first_dice == 4:
            return pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice4.xcf")
        if first_dice == 5:
            return pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice5.xcf")
        if first_dice == 6:
            return pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice6.xcf")

