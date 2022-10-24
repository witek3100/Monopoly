import sys
import pygame
from player import Player
from buttons import Button
import random

pygame.init()
board = pygame.image.load("board.png")

class Game:

    def __init__(self, players, screen):
        self.screen = screen
        self.players = [Player(i) for i in range(players)]
        self.board = []
        self.buttons = []
        self.turn = 0

    def player_turn(self, player):
        c = random.randint(1,5)
        player.move(c)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            for button in self.buttons:
                button.draw(self.screen)
                button.check_click(event)

    def game_loop(self):
        while True:
            self.draw()
            self.handle_events()
            for i in self.players:
                button_font = pygame.font.Font(None, 30)
                self.buttons.append(Button('DICE', (100, 50), (10, 10), 5, button_font))
                if self.buttons[0].pressed:
                    self.player_turn(i)
                    self.buttons.pop()
            pygame.display.update()

    def draw(self):
        self.screen.fill((30,30,30))
        self.screen.blit(board, (300, 100))
        for button in self.buttons:
            button.draw(self.screen)
        for player in self.players:
            player.draw(self.screen)