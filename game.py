import sys
import pygame

import boardFieldsData
from button import Button
from player import Player
from board_fields import *

class Game:

    board_fields_data = [()]

    def __init__(self, screen):
        self.screen = screen
        self.players = [Player(self.screen, num) for num in range(1)]
        self.objects_to_display = []
        self.board_fields = [BoardField(self.screen, bf[0], bf[1]) for bf in boardFieldsData.fields_data]
        self.buttons = [Button(self.screen, (10, 10), (140, 70), "DICE")] + [bf.button for bf in self.board_fields]


    def game_loop(self):
        board = pygame.image.load("board.xcf")
        run = True
        while run:
            self.screen.fill((0, 100, 0))
            self.screen.blit(board, (300, 70))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            for player in self.players:
                player.draw()
                if self.buttons[0].action():
                    self.objects_to_display += player.move()

            for object in self.objects_to_display:
                self.screen.blit(object[0], object[1])

            for button in self.buttons:
                button.draw()
                button.action()

            pygame.display.update()