import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")

PLAYER_WIDTH, PLAYER_HEIGHT = 100, 100

PLAYER_IMAGE = pygame.image.load(os.path.join('assets\sprites\hero\idle\hero-idle-front\hero-idle-front.png'))
PLAYER = pygame.transform.rotate(pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
VEL = 5

def draw(player):

    WIN.fill(BLACK)
    WIN.blit(PLAYER, (player.x, player.y))
    
    pygame.display.update()


def player_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # Left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + PLAYER_WIDTH < WIDTH//2: # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + PLAYER_HEIGHT < HEIGHT - 15: # Down
        yellow.y += VEL


def main():

    # Initial Settings
    clock = pygame.time.Clock()
    run = True

    # Setup 
    player = pygame.Rect(100, 300, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player)

        draw(player)

    main()



if __name__ == "__main__":
    main()