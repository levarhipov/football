import pygame
import sys

from ball import Ball
from player import Player

players = dict()


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("футбол")
    bg_color = (34, 139, 34)

    player1 = Player(screen, "Z")
    player2 = Player(screen, "X")
    player3 = Player(screen, "C")

    player2.is_active = True

    players[pygame.K_z] = player1
    players[pygame.K_x] = player2
    players[pygame.K_c] = player3

    ball = Ball(screen)

    while True:
        for event in pygame.event.get():
            handle_event(player1, event)
            player1.update()
            handle_event(player2, event)
            player2.update()
            handle_event(player3, event)
            player3.update()

            active_player = get_active_player(players)
            ball.update(active_player)

        screen.fill(bg_color)
        player1.output()
        player2.output()
        player3.output()
        ball.output()
        pygame.display.flip()


def get_active_player(all_players):
    for p in all_players.values():
        if p.is_active:
            return p


def handle_event(player, event):
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
