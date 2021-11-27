import pygame
import os
from player import Player

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")

# PLAYER = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)

FPS = 60

def draw(player):

    WIN.fill('black')
    
    WIN.blit(player.image, (player.rect.x, player.rect.y))

    pygame.display.update()


def main():

    # Initial Settings
    clock = pygame.time.Clock()
    run = True

    # Setup 
    player = Player((100, 300))

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        player.update()
        
        draw(player)

    main()


if __name__ == "__main__":
    main()