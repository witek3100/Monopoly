import pygame


class Button:
    def __init__(self, screen, pos, size):
        self.screen = screen
        self.position = pos
        self.size = size
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.normal_color = (205,51,51)
        self.hovered_color = (238,59,59)
        self.color = self.normal_color
        self.pressed = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position, self.size))

    def action(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.color = self.hovered_color
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.pressed = True
                action = True
        else:
            self.color = self.normal_color

        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False

        return action