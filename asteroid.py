import pygame
import random
from constants import *
import circleshape
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        pos_vector = self.velocity.rotate(random_angle)
        neg_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position[0],self.position[1],new_radius)
        asteroid_one.velocity = pos_vector * 1.2
        asteroid_two = Asteroid(self.position[0],self.position[1],new_radius)
        asteroid_two.velocity = neg_vector * 1.2