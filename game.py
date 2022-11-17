import sys
import boardFieldsData
from board_fields import *
from button import Button

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.players = [Player(self.screen, num) for num in range(1)]
        self.objects_to_display = []
        self.board_fields = [DistrictField(self.screen, bf[1], bf[2], bf[0]) if bf[0] == "DF" else BoardField(self.screen, bf[1], bf[2], bf[0]) for bf in boardFieldsData.fields_data]
        self.buttons = [Button(self.screen, (20, 20), (140, 70), "DICE")]
        self.dices = []

    def game_loop(self):
        board = pygame.image.load("photos/board.xcf")
        run = True
        player = self.players[0]
        mv = True
        ac = False
        while run:
            self.screen.fill((0, 100, 0))
            self.screen.blit(board, (300, 70))
            self.screen.blit(pygame.font.SysFont("money_font", 50).render(str(player.money),False,(238, 59, 59)), (200, 700))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            for button in self.buttons:
                button.draw()

            if mv:
                if self.buttons[0].action():
                    self.objects_to_display += player.move(self)
                    ac = True
                    mv = False

            for dice in self.dices:
                self.screen.blit(dice[0], dice[1])

            for object in self.objects_to_display:
                self.screen.blit(object[0], object[1])

            for f in self.board_fields:
                if f.show_information():
                    self.objects_to_display.append([f.image, (500, 200)])

            if ac:
                self.board_fields[player.position].action(player)
                ac = False
                mv = True

            player.draw()

            for i, color in enumerate(player.own_districts):
                for j, dc in enumerate(player.own_districts[color]):
                    self.objects_to_display.append([pygame.transform.scale(dc.image, (85, 135)), (400 + (i * 60), 650 + (j * 30))])

            pygame.display.update()