import pygame
from constants import *
from circleshape import CircleShape
# Bullet class for the Asteroids game

class Shot(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        #self.velocity = pygame.Vector2(0, 1).rotate(.rotation) * BULLET_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)
    
    def update(self, dt):
        # Update the position based on velocity
        self.position += self.velocity * dt