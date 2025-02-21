# stdlib
import pygame
# constants
from player import Player
import constants
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))    
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable) # magic? this gets added to the groups above?
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # Game clock and delta time
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update player before rendering
        # player.update(dt)
        
        # after making updatable group, calling the method with the group itself will make all objects in a group call that method
        # review it here: https://www.boot.dev/lessons/6a09887c-ad3f-4fb3-8726-c7bd9fa4161c
        updatable.update(dt)
        
        # rendering
        screen.fill("black")
        # player.draw(screen) 
        # similarly doing it, BUT iterate!
        for drawable_obj in drawable:
            drawable_obj.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()