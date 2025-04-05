import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Bullet

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    
    # Initialize the player
    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  
    # Initialize the player and asteroid field
    # Set up the containers for the sprites
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Bullet.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in asteroids:
            if player.check_collision(sprite):
                print("Game Over!")
                sys.exit(0)
            for shot in shots:
                if shot.check_collision(sprite):
                    # Remove the asteroid and bullet
                    sprite.kill()
                    shot.kill()
                    # Optionally, you can add a score or explosion effect here
                    print("Asteroid hit!")
                # Handle collision (e.g., end game, reduce health, etc.)
                # For now, just print a message
                
        
        
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = game_clock.tick(60) / 1000.0
       
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()