import pygame


class Gate:

    def __init__(self, screen, name):
        self.screen = screen
        self.image = pygame.image.load('images/gate.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.rect.height

    def output(self):
        """рисование ворот"""
        self.screen.blit(self.image, self.rect)
