#This is the file for the ship
# and all of its settings and
#loading so here we go

import pygame

class Ship:

    def __init__(self, ai_game) :
        #We're initializing a ship and giving it a starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #initializing the settings
        self.settings = ai_game.settings

        #This loads the ships image and gets how big it is
        self.image = pygame.image.load('images/ship.bmp') 
        self.rect = self.image.get_rect()

        #we'll be starting the ship at the bottom and center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Storing the ship's horizontal position in a float
        self.x = float(self.rect.x)

        #We need a movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_a = False
        self.moving_d = False

    def update(self) :
        """This updates the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        if self.moving_d and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed

        if self.moving_a and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self) :
        """Centering the ship at the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self) :
        #This draws the ship at its current location
        self.screen.blit(self.image, self.rect)

