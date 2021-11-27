import pygame
from settings import tile_size
from tiles import Tile
from player import Player

class Level():
    def __init__(self, level_data, surface):
        super().__init__()
        
        # Level Setup
        self.display_surface = surface 
        self.setup_level(level_data)

    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = Player((100, 300))

        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size

                if (cell == ' '):
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_surface)

        self.player.update()
        
        self.display_surface.blit(self.player.image, (self.player.rect.x, self.player.rect.y))

        #for tile in self.tiles:
         #   self.display_surface.blit(tile.image, (tile.rect.x, tile.rect.y))
    