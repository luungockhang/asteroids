# stdlib
import pygame
import sys
# constants
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from player import Player
import constants
from constants import *

def main():
    # ==== Initialization ===
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))    
    
    # Groups
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Containers
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable) # magic? this gets added to the groups above?
    
    # Object creation
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    # Game clock and delta time
    clock = pygame.time.Clock()
    dt = 0
    
    # ==== Game loop ====
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update player before rendering
        # player.update(dt)
        # after making updatable group, calling the method with the group itself will make all objects in a group call that method
        # review it here: https://www.boot.dev/lessons/6a09887c-ad3f-4fb3-8726-c7bd9fa4161c
        updatable.update(dt)
        
        # Collision check
        for asteroid_obj in asteroids:
            if asteroid_obj.collide(player):
                print(asteroid_obj.collide(player))
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid_obj.collide(shot):
                    shot.kill()
                    asteroid_obj.split()

        
        # Rendering
        
        screen.fill("black")
        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()