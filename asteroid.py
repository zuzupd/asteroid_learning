import pygame # type: ignore
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid = Asteroid(self.position.x, self.position.y, radius=self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = self.velocity.rotate(angle) * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, radius=self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = self.velocity.rotate(-angle) * 1.2
