import pygame


class Ball:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.is_active = False
        
    def update(self, player):
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery

    def output(self):
        """рисование мяча"""
        self.screen.blit(self.image, self.rect)
