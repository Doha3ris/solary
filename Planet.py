import math
import random


class Planet:
    def __init__(self, x, y, radius, color, distanceFromCenter):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.radians = random.random() * math.pi * 2
        self.velocity = 1 / distanceFromCenter * 3
        self.distanceFromCenter = distanceFromCenter

    def orbit(self):
        self.radians += self.velocity
        self.x = 512 + math.cos(self.radians) * self.distanceFromCenter
        self.y = 384 + math.sin(self.radians) * self.distanceFromCenter
