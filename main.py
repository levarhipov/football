import pygame
import sys
from player import Player

players = dict()


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("футбол")
    bg_color = (34, 139, 34)
    player1 = Player(screen)
    player2 = Player(screen)
    player3 = Player(screen)

    players[pygame.K_z] = player1
    players[pygame.K_x] = player2
    players[pygame.K_c] = player3

    while True:
        events(player2)
        player2.update_player()
        events(player1)
        player1.update_player()
        events(player3)
        player3.update_player()

        screen.fill(bg_color)
        player1.output()
        player2.output()
        player3.output()

        pygame.display.flip()


def events(player):
    """обработка событий"""
    for event in pygame.event.get():
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