import sys
import boardFieldsData
from board_fields import *

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.players = [Player(self.screen, num) for num in range(1)]
        self.objects_to_display = []
        self.board_fields = [BoardField(self.screen, bf[1], bf[2]) if bf[0] else DistrictField(self.screen, bf[1], bf[2]) for bf in boardFieldsData.fields_data]
        self.buttons = [Button(self.screen, (10, 10), (140, 70), "DICE")]

    def game_loop(self):
        board = pygame.image.load("photos/board.xcf")
        run = True
        while run:
            self.screen.fill((0, 100, 0))
            self.screen.blit(board, (300, 70))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.buttons[0].draw()
            for player in self.players:
                player.draw()
                if self.buttons[0].action():
                    self.objects_to_display.clear()
                    self.objects_to_display += player.move()
                    self.board_fields[player.position].action(player)
                    self.objects_to_display.append([(pygame.font.SysFont("money_font", 50).render(str(player.money), False, (238,59,59))), (400, 700)])


            for object in self.objects_to_display:
                self.screen.blit(object[0], object[1])

            for f in self.board_fields:
                if f.show_information():
                    self.objects_to_display.append([f.image, (500, 200)])

            pygame.display.update()