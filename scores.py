import pygame.font


class Scores:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (93, 196, 50)
        self.font = pygame.font.SysFont(None, 44)
        self.strikes = 0
        self.hits = 0
        self.image_score()

    def image_score(self):
        # надо чтобы цифра рисовалась для strikes и hits отдельно
        # сделать strikes_img и strikes_rect для подсчёта ударов
        # сделать hits_img и hits_rect для подсчёта голов
        # у hits_rect и strikes_rect должны быть разные координаты на экране
        self.score_img = self.font.render(str(self.strikes), True, self.text_color, (34, 139, 34))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 60
        self.score_rect.top = 20

    def output(self):
        self.screen.blit(self.score_img, self.score_rect)
