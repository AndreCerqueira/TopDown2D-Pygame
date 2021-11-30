import pygame
from settings import * 
from level import Level

pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")
clock = pygame.time.Clock()
level = Level(level_map, WIN)

def main():

    # Setup 
    level = Level(level_map, WIN)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        level.run()

        clock.tick(FPS)
        pygame.display.update()        


if __name__ == "__main__":
    main()