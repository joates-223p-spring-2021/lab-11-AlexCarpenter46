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
        self.settings = ai_game.settings

        #loading alien image and it's rect attributes
        self.image = pygame.image.load('images/alien.bmp') 
        self.rect = self.image.get_rect()

        #Spawn the aliens at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #get the alien's horizontal position
        self.x = float(self.rect.x) 

    def check_edges(self) :
        """Returns true if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0 :
            return True

    def update(self) :
        """Moving the aliens time"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
