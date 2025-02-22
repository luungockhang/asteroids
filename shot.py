import pygame
from constants import *
import circleshape
from circleshape import CircleShape

class Shot(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def draw(self,screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, width=2)