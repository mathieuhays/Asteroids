from re import purge

import pygame
from pygame import Color

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = Color(0, 0, 0)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update
        # updatable.update(dt)
        pygame.sprite.Group.update(updatable, dt)

        # draw
        screen.fill(black)
        # drawable.draw(screen)
        for sprite in pygame.sprite.Group.sprites(drawable):
            sprite.draw(screen)

        #pygame.sprite.Group.draw(drawable, screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()