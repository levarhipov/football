import pygame.font


class Scores:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (93, 196, 50)
        self.font = pygame.font.SysFont(None, 44)
        self.strikes = 0
        self.hits = 0
        self.update()

    def update(self):
        self.strikes_img = self.font.render("Strikes: " + str(self.strikes), True, self.text_color, (34, 139, 34))
        self.strikes_rect = self.strikes_img.get_rect()
        self.strikes_rect.right = self.screen_rect.right - 60
        self.strikes_rect.top = 20

        self.hits_img = self.font.render("Hits: " + str(self.hits), True, self.text_color, (34, 139, 34))
        self.hits_rect = self.hits_img.get_rect()
        self.hits_rect.left = self.screen_rect.left + 60
        self.hits_rect.top = 20

    def output(self):
        self.screen.blit(self.strikes_img, self.strikes_rect)
        self.screen.blit(self.hits_img, self.hits_rect)
