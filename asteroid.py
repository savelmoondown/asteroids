import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, pygame.Vector2(0, 0))
        self.radius = radius
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt