#This file controls the aliens and spawns
#them at the top of the screen

import pygame
from pygame.sprite import Sprite

class Alien(Sprite) :
    """This class creates a single alien"""

    def __init__(self, ai_game) :
        """Initializing the alien and giving it a starting position"""
        #once again we use super() to properly inherit from sprite
        super().__init__()
            
        self.screen = ai_game.screen

        #loading alien image and it's rect attributes
        self.image = pygame.image.load('images/alien.bmp') 
        self.rect = self.image.get_rect()

        #Spawn the aliens at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #get the alien's horizontal position
        self.x = float(self.rect.x) 


