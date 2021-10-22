import math
import random

import pygame

from Planet import Planet

pygame.init()

w, h = 1024, 768
x, y = w / 2, h / 2
screen = pygame.display.set_mode((w, h))

planets = [
    Planet(x, y, 5, (200, 200, 200), 80),
    Planet(x, y, 10, (255, 165, 0), 110),
    Planet(x, y, 10, (0, 0, 255), 140),
    Planet(x, y, 5, (255, 0, 0), 170),
    Planet(x, y, 20, (191, 177, 119), 220),
    Planet(x, y, 20, (128, 0, 128), 280),
    Planet(x, y, 12, (78, 160, 163), 330),
    Planet(x, y, 12, (12, 22, 255), 370),
]

play = True

clock = pygame.time.Clock()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # RETRIEVE THE MOUSE'S POSITION
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            # DISTANCE FORMULA
            dx = (mouseX - sun.x) ** 2
            dy = (mouseY - sun.y) ** 2
            if math.sqrt(dx + dy) < sun.radius and len(planets) > 1:
                planets.pop(len(planets) - 1)
            else:
                planets.append(
                    Planet(
                        mouseX,
                        mouseY,
                        random.randrange(5, 10),
                        (random.randrange(255), random.randrange(255), random.randrange(255)),
                        (random.randrange(80, 400))
                    )
                )
        if len(planets) <= 42:
            backgroundImage = pygame.image.load("space.jpeg")
        else:
            backgroundImage = pygame.image.load("beer.jpeg")
        if event.type == pygame.KEYUP:
            print(event.key, event.unicode, event.scancode)
            if event.key == pygame.K_ESCAPE:
                play = False

    screen.fill((0, 0, 0))
    screen.blit(backgroundImage, [0, 0])

    sun = Planet(x, y, 50, (252, 212, 64), 0.01)
    pygame.draw.circle(screen, sun.color, (sun.x, sun.y), sun.radius)

    for planet in planets:
        pygame.draw.circle(screen, planet.color, (planet.x, planet.y), planet.radius)
        planet.orbit()

    clock.tick(60)
    pygame.display.flip()
