import pygame

WHITE = (255, 255, 255)

class Button:
    def __init__(self, text, size, pos, elev, button_font):
        self.pressed = False
        self.elevation = elev
        self.dyanimc_elecation = elev
        self.original_y_pos = pos[1]

        self.top_rect = pygame.Rect(pos, size)
        self.top_color = (10, 10, 250)

        self.bottom_rect = pygame.Rect(pos, size)
        self.bottom_color = (200, 200, 200)

        self.text = text
        self.text_surf = button_font.render(str(text), True, WHITE)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen):
        self.top_rect.y = self.original_y_pos - self.dyanimc_elecation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyanimc_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect)
        pygame.draw.rect(screen, self.top_color, self.top_rect)

        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (150, 150, 150)
            if pygame.mouse.get_pressed()[0]:
                self.dyanimc_elecation = 0
                self.pressed = True
            else:
                self.dyanimc_elecation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dyanimc_elecation = self.elevation
            self.top_color = (150, 150, 150)


