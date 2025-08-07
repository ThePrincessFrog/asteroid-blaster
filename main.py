import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.collides(player):
                sys.exit("Game over!")
            for bullet in shots:
                if item.collides(bullet):
                    item.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
