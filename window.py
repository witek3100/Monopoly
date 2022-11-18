import time

from button import Button
import pygame
import sys

class Window:

    def __init__(self, screen, text):
        self.screen = screen
        self.text = text
        self.color = (139,69,19)
        self.size = (0, 0)
        self.win_rect = pygame.Rect(390, 240, self.size[0], self.size[1])

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.win_rect.bottomleft, 20)
        pygame.draw.circle(self.screen, self.color, self.win_rect.bottomright, 20)
        pygame.draw.circle(self.screen, self.color, self.win_rect.topright, 20)
        pygame.draw.circle(self.screen, self.color, self.win_rect.topleft, 20)
        pygame.draw.rect(self.screen, self.color, ((self.win_rect.topleft[0] - 20, self.win_rect.topleft[1]), (self.win_rect.size[0] + 40, self.win_rect.size[1])))
        pygame.draw.rect(self.screen, self.color, ((self.win_rect.topleft[0], self.win_rect.topleft[1] - 20), (self.win_rect.size[0], self.win_rect.size[1] + 40)))

    def action(self):
        pass

class Buy_district_window(Window):

    def __init__(self, screen, text):
        super().__init__(screen, text)
        self.size = (450, 200)
        self.win_rect = pygame.Rect(390, 240, self.size[0], self.size[1])
        self.buttons = [Button(self.screen, (self.win_rect.bottomleft[0] + 20, self.win_rect.bottomleft[1] - 80), (100, 60), "YES"), Button(self.screen, (self.win_rect.bottomright[0] - 120, self.win_rect.bottomright[1] - 80), (100, 60), "NO")]

    def action(self) -> bool:

        self.draw()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            text = pygame.font.SysFont("buy font", 30).render(self.text[0], False, (0, 0, 0))
            self.screen.blit(text, (self.win_rect.topleft[0] + 20, self.win_rect.topleft[1] + 20))

            text = pygame.font.SysFont("buy font", 30).render(self.text[1], False, (0, 0, 0))
            self.screen.blit(text, (self.win_rect.topleft[0] + 20, self.win_rect.topleft[1] + 55))

            for button in self.buttons:
                button.draw()
            if self.buttons[0].action():
                return True
            if self.buttons[1].action():
                return False
            pygame.display.update()


class Card_window(Window):

    def __init__(self, screen, text, district, player):
        super().__init__(screen, text)
        self.size = (500, 450)
        self.player = player
        self.district = district
        self.win_rect = pygame.Rect(390, 240, self.size[0], self.size[1])
        self.buttons = [Button(self.screen, (self.win_rect.bottomleft[0] + 10, self.win_rect.bottomleft[1] - 80), (120, 60), "BUY HOUSE"),
                        Button(self.screen, (self.win_rect.midbottom[0] - 60, self.win_rect.bottomright[1] - 80), (120, 60), "PAWN"),
                        Button(self.screen, (self.win_rect.bottomright[0] - 130, self.win_rect.bottomright[1] - 80), (120, 60), "QUIT")]
        self.buttons[0].active = False
        self.buttons[1].active = False

    def action(self):
        self.draw()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            text = pygame.font.SysFont("buy font", 30).render(self.text[0], False, (0, 0, 0))
            self.screen.blit(text, (self.win_rect.topleft[0] + 20, self.win_rect.topleft[1] + 20))

            card_img = self.district.image
            self.screen.blit(card_img, (self.win_rect.midtop[0] - (card_img.get_width()/2), self.win_rect.midright[1] - (card_img.get_height() /2)))

            if self.district.color in self.player.own_districts:
                if self.district.owner == self.player:
                    self.buttons[1].active = True
                    if len(self.player.own_districts.get(self.district.color)) == self.district.color_dis_am:
                        self.buttons[0].active = True

            for button in self.buttons:
                button.draw()
            if self.buttons[0].action():
                self.district.buy_house()
            if self.buttons[1].action():
                self.district.pawn()
            if self.buttons[2].action():
                break


            pygame.display.update()