import pygame

fields_positions = [[830, 650],[770, 650],[725, 650],[680, 650],[635, 650], [590, 650], [545, 650], [500, 650], [455, 650],[410, 650],[340, 650],
                    [340, 585],[340, 540],[340, 495],[340, 450],[340, 405], [340, 360], [340, 315], [340, 270], [340, 225],[340, 180],[340, 135],
                    [340, 150],[410, 150],[455, 150],[500, 150],[545, 150], [590, 150], [635, 150], [680, 150], [725, 150],[770, 150],[830, 150],
                    ]

class Player:

    def __init__(self, number):
        self.number = number
        self.money = 0
        self.position = 0
        self.own_districts = []

    def move(self, x):
        self.position = (self.position + x) % 30

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 215, 0), (fields_positions[self.position],(30,30)))

