import pygame
import sys

from ball import Ball
from defender import Defender
from player import Player

players = dict()


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("футбол")
    bg_color = (34, 139, 34)

    defender1 = Defender(screen, "[PlaceHolder1]")
    defender1.rect.centery = 200
    defender1.rect.centerx = 300
    defender2 = Defender(screen, "[PlaceHolder2]")
    defender2.rect.centery = 50
    defender2.rect.centerx = 600
    defender3 = Defender(screen, "[PlaceHolder3]")
    defender3.rect.centery = 200
    defender3.rect.centerx = 900

    player1 = Player(screen, "Z")
    player1.rect.centery = 500
    player1.rect.centerx = 300
    player2 = Player(screen, "X")
    player2.rect.centery = 600
    player2.rect.centerx = 600
    player3 = Player(screen, "C")
    player3.rect.centery = 500
    player3.rect.centerx = 900

    player2.is_active = True

    players[pygame.K_z] = player1
    players[pygame.K_x] = player2
    players[pygame.K_c] = player3

    ball = Ball(screen)

    while True:
        for event in pygame.event.get():
            defender1.update()
            defender2.update()
            defender3.update()
            handle_event(event, player1, ball)
            player1.update()
            handle_event(event, player2, ball)
            player2.update()
            handle_event(event, player3, ball)
            player3.update()

            active_player = get_active_player(players)
            ball.update(active_player)

        screen.fill(bg_color)
        defender1.output()
        defender2.output()
        defender3.output()
        player1.output()
        player2.output()
        player3.output()
        ball.output()
        pygame.display.flip()


def get_active_player(all_players):
    for p in all_players.values():
        if p.is_active:
            return p


def handle_event(event, player, ball):
    """обработка событий"""

    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            player.mright = True
        elif event.key == pygame.K_LEFT:
            player.mleft = True
        elif event.key == pygame.K_UP:
            player.mup = True
        elif event.key == pygame.K_DOWN:
            player.mdown = True
        else:
            selected = players.get(event.key)
            if selected is not None:
                for p in players.values():
                    p.is_active = False
                selected.is_active = True
                ball.is_active = True

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            player.mright = False
        elif event.key == pygame.K_LEFT:
            player.mleft = False
        elif event.key == pygame.K_UP:
            player.mup = False
        elif event.key == pygame.K_DOWN:
            player.mdown = False


run()
