import pygame
import boardFieldsData
import random

class Player:

    def __init__(self, screen, num):
        self.screen = screen
        self.number = num
        self.position = 0
        self.in_jail = 0

        self.money = 1500
        self.own_districts = {}

    def draw(self):
        pygame.draw.rect(self.screen, (255,185,15), (boardFieldsData.fields_data[self.position][2][0], (20, 20)))

    def move(self, game):

        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)

        tab = []

        while second_dice == first_dice:
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)

        if self.position + first_dice + second_dice >= 40:
            self.money += 200

        self.position = (self.position + first_dice + second_dice) % 40

        self.draw()
        pygame.display.update()

        if first_dice == 1:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice1.xcf"), (100, 200)])
        if first_dice == 2:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice2.xcf"), (100, 200)])
        if first_dice == 3:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice3.xcf"), (100, 200)])
        if first_dice == 4:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice4.xcf"), (100, 200)])
        if first_dice == 5:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice5.xcf"), (100, 200)])
        if first_dice == 6:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice6.xcf"), (100, 200)])


        if second_dice == 1:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice1.xcf"), (100, 400)])
        if second_dice == 2:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice2.xcf"), (100, 400)])
        if second_dice == 3:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice3.xcf"), (100, 400)])
        if second_dice == 4:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice4.xcf"), (100, 400)])
        if second_dice == 5:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice5.xcf"), (100, 400)])
        if second_dice == 6:
            tab.append([pygame.image.load("/home/witek/PycharmProjects/Monopoly/photos/dice6.xcf"), (100, 400)])

        return tab

    def lock_in_prison(self):
        self.in_jail += 3
        self.position = 10
