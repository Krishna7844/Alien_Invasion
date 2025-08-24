import pygame
from pygame.sprite import Sprite

class RainDrops(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        original_image = pygame.image.load("/Users/krishna/Desktop/hacker rank/pygame/images/raindrops.bmp")
        self.image = pygame.transform.scale(original_image, (16,16))
        # self.image = pygame.image.load("/Users/krishna/Desktop/hacker rank/pygame/images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
