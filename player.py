import random

import pygame


class Player:

    def __init__(self, screen):
        """иницилизация игрока"""

        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - random.randint(10, self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom - random.randint(10, self.screen_rect.centery)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.is_active = False

    def output(self):
        """рисование игрока"""
        self.screen.blit(self.image, self.rect)

    def update_player(self):
        """обновление позиции игрока"""
        if not self.is_active:
            return

        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 5
        if self.mup and self.rect.bottom > self.rect.height:
            self.rect.centery -= 5
        if self.mdown and self.rect.bottom < + self.screen_rect.bottom:
            self.rect.centery += 5

    def __repr__(self):
        return "Is active: " + str(self.is_active)