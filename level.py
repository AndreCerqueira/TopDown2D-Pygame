import pygame
from settings import WIDTH, tile_size
from tiles import Tile
from player import Player
from pytmx.util_pygame import load_pygame

class Level():
    def __init__(self, level_data, surface):
        super().__init__()
        
        # Level Setup
        self.tmxdata = load_pygame("levels/level_data/level_0.tmx")
        self.display_surface = surface 
        self.player = Player((100, 300))

    
    def setup_level(self):
        for layer in self.tmxdata:
            for tile in layer.tiles():
                x_pixel = tile[0] * 64
                y_pixel = tile[1] * 64
                self.display_surface.blit(tile[2], (x_pixel, y_pixel))

    def draw_level(self):
        pass

    def scroll_map(self):
        player_x = self.player.rect.centerx
        direction_x = self.player.direction.x

        if player_x < WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            self.player.speed = 0
        elif player_x > WIDTH - (WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            self.player.speed = 0
        else:
            self.world_shift = 0
            self.player.speed = 8


    def run(self):

        self.player.update()

        self.scroll_map()
        
        self.setup_level()
        self.display_surface.blit(self.player.image, self.player.rect)


