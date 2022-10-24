import pygame




class Button:
    def __init__(self, text, size, pos, elev, button_font):
        self.pressed = False
        self.elevation = elev
        self.dyanimc_elecation = elev
        self.original_y_pos = pos[1]

        self.top_rect = pygame.Rect(pos, size)
        self.top_color = (205,51,51)

        self.bottom_rect = pygame.Rect(pos, size)
        self.bottom_color = (139,35,35)

        self.text = text
        self.text_surf = button_font.render(str(text), True, (250, 200, 250))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen):
        self.top_rect.y = self.original_y_pos - self.dyanimc_elecation
        self.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyanimc_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect)
        pygame.draw.rect(screen, self.top_color, self.top_rect)

        screen.blit(self.text_surf, self.text_rect)

    def check_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (255,64,64)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dyanimc_elecation = 0
                self.pressed = True
            else:
                self.dyanimc_elecation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dyanimc_elecation = self.elevation
            self.top_color = (205, 51, 51)