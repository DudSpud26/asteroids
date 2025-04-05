import pygame
from constants import *
from circleshape import CircleShape
import random
# Asteroid class for the Asteroids game

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)
    
    def update(self, dt):
        # Update the position based on velocity
        self.position += self.velocity * dt
        
    def split(self):
        # Split the asteroid into smaller ones
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)
        new_radius = self.radius -ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_one * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = vector_two * 1.2