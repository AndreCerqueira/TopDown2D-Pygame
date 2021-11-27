import pygame
from settings import * 
from level import Level

pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")
clock = pygame.time.Clock()
level = Level(level_map, WIN)

# PLAYER = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)

def main():

    # Setup 
    level = Level(level_map, WIN)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WIN.fill('black')

        level.run()
        
        clock.tick(FPS)
        pygame.display.update()
        
        


if __name__ == "__main__":
    main()