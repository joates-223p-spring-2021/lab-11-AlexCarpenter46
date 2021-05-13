#This is the file that handles the bullets
#that the ship will shoot at the aliens

import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite) :
    """This class manages bullets fired from the ship"""

    def __init__(self, ai_game) :
        """This creates a bullet object at the ship's current position"""

        #calling super apparently inherits properly from sprite
        super().__init__()

        #all the settings from settings.py
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Creating a bullet rect at (0, 0) and then setting it to the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #storing the bullets position as decimal for smoothness i'm guessing
        self.y = float(self.rect.y)


    def update(self) :
        """This updates the bullets position on the screen"""

        #update the decimal position of the bullet. 
        self.y -= self.settings.bullet_speed

        #updating the rect position
        self.rect.y = self.y 


    def draw_bullet(self) :
        """Drawing the bullet to the screen""" 
        pygame.draw.rect(self.screen, self.color, self.rect)

