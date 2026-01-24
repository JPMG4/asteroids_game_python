import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    """Class representing an asteroid in the game."""
    def __init__(self, x, y, radius, *args):
        super().__init__(x, y, radius)
        

    def draw(self, surface):
        pygame.draw.circle(surface, ("white"), self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        """Splits the asteroid into smaller asteroids if possible."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector2 * 1.2
        