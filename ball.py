import pygame
from pygame.sprite import Group


class Ball(pygame.sprite.Sprite):

    def __init__(self, screen, score):
        super(Ball, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.target = None
        self.is_pass = False
        self.is_strike = False
        self.score = score

    def update(self, player, defenders):
        if self.is_pass:
            diffx = abs(self.rect.centerx - player.rect.centerx)
            diffy = abs(self.rect.centery - player.rect.centery)

            mulx = 1 if player.rect.centerx > self.rect.centerx else -1
            muly = 1 if player.rect.centery > self.rect.centery else -1

            speed = 5
            self.rect.centerx = self.rect.centerx + (mulx * diffx / speed)
            self.rect.centery = self.rect.centery + (muly * diffy / speed)

            if abs(self.rect.centerx - player.rect.centerx) < speed \
                    and abs(self.rect.centery - player.rect.centery) < speed:
                self.is_pass = False
        elif self.is_strike:
            target_rect = self.target
            diffx = abs(self.rect.centerx - target_rect.centerx)
            diffy = abs(self.rect.centery - target_rect.centery)

            mulx = 1 if target_rect.centerx > self.rect.centerx else -1
            muly = 1 if target_rect.centery > self.rect.centery else -1

            speed = 7
            self.rect.centerx = self.rect.centerx + (mulx * diffx / speed)
            self.rect.centery = self.rect.centery + (muly * diffy / speed)

            if pygame.sprite.spritecollideany(self, Group(defenders)):
                self.is_strike = False

            if abs(self.rect.centerx - target_rect.centerx) < speed \
                    and abs(self.rect.centery - target_rect.centery) < speed:
                self.is_strike = False
                self.score.hits += 1
                self.score.update()
        else:
            self.rect.centerx = player.rect.centerx
            self.rect.centery = player.rect.centery

    def output(self):
        """рисование мяча"""
        self.screen.blit(self.image, self.rect)
