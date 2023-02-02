import random
import pygame


class Defender:

    def __init__(self, screen, name):

        self.name = name
        self.screen = screen
        self.image = pygame.image.load('images/red.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - random.randint(10, self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom - random.randint(10, self.screen_rect.centery)
        self.mright = True
        self.mleft = False
        self.is_active = False
        self.counter = 0

    def output(self):
        """рисование защитника"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """обновление позиции защитника"""

        speed = 2
        if self.mright:
            self.rect.centerx += speed
            self.counter += 1
            if self.counter == 60:
                self.mright = False
                self.mleft = True

        if self.mleft:
            self.rect.centerx -= speed
            self.counter -= 1
            if self.counter == -60:
                self.mright = True
                self.mleft = False

    def __repr__(self):
        return self.name + " is active: " + str(self.is_active)
