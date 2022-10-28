import sys
import pygame
from button import Button
from player import Player


class Game:

    board_fields_data = [()]

    def __init__(self, screen):
        self.screen = screen
        self.players = [Player(self.screen, num) for num in range(1)]

    def game_loop(self):
        board = pygame.image.load("board.xcf")
        button = Button(self.screen, (10, 10), (140, 70), "DICE")
        run = True
        while run:
            self.screen.fill((0, 100, 0))
            self.screen.blit(board, (300, 70))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for player in self.players:
                player.draw()
                if button.action():
                    player.move(50)
            button.draw()
            pygame.display.update()