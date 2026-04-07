from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rotation_number = random.uniform(20, 50)
        first_asteroid_velocity = self.velocity.rotate(rotation_number)
        second_asteroid_velocity = self.velocity.rotate(-rotation_number)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # we pass self.position.x as the variable is neither attached to parent nor the current class
        # TRICKY
        # CONCEPT
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_asteroid_velocity * 1.2
        second_asteroid.velocity = second_asteroid_velocity * 1.2
        
