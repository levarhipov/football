import random
import pygame


class Player:

    def __init__(self, screen, name):
        """иницилизация игрока"""
        self.name = name
        self.screen = screen
        self.image = pygame.image.load('images/blue.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - random.randint(10, self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom - random.randint(10, self.screen_rect.centery)
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.is_active = False
        self.font = pygame.font.SysFont(None, 36)

    def output(self):
        """рисование игрока"""
        self.screen.blit(self.image, self.rect)
        self.label_img = self.font.render(str(self.name), True, (0, 255, 255), (80, 160, 234))
        self.label_rect = self.label_img.get_rect()
        self.label_rect.centerx = self.rect.centerx
        self.label_rect.centery = self.rect.centery
        self.screen.blit(self.label_img, self.label_rect)

    def update(self):
        """обновление позиции игрока"""
        if not self.is_active:
            return

        speed = 10
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += speed
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= speed
        if self.mup and self.rect.bottom > self.rect.height:
            self.rect.centery -= speed
        if self.mdown and self.rect.bottom < + self.screen_rect.bottom:
            self.rect.centery += speed

    def __repr__(self):
        return self.name + " is active: " + str(self.is_active)

    