#This is Alien Invasion which is based on the
#Alien invasion project in Python Crash Course
#Author is Alex Carpenter
#CPSC 223P 
#May 5th, 2021

import sys 
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
     
    def __init__(self) :
        """Initializing function that calls all the needed function"""

        #initializing the game
        pygame.init()

        #settings
        self.settings = Settings()

        #this is screen size
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        #have to initialize the ship
        self.ship = Ship(self) 

        #inintializing the bullets
        self.bullets = pygame.sprite.Group()

        #initializing aliens
        self.aliens = pygame.sprite.Group()

        #creating aliens
        self.create_fleet()

        #screen name
        pygame.display.set_caption("Alien Invasion") 

    def run_game(self) :
        """Main loop that runs the game and draws the game to the screen"""

        while True :
            
            #checks for events
            self.check_events()
            
            #updates screen accordingly
            self.update_screen()

            #and update the ship
            self.ship.update()

            #updating the bullets and deleting old ones
            self.update_bullets()

            pygame.display.flip()

    def check_events(self) :
        """This handles key presses and updates accordingly"""
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()

            #this controls key down presses
            elif event.type == pygame.KEYDOWN :
                self.check_keydown_events(event)

            #this controls key release events
            elif event.type == pygame.KEYUP :
                self.check_keyup_events(event)

    
    def check_keydown_events(self, event) :
        """This function handles key down presses"""
        if event.key == pygame.K_RIGHT :
            #this moves the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT :
            #this moves the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE :
            #this handles firing the bullets
            self.fire_bullet()

    def check_keyup_events(self, event) :
        """This function handles key release events"""
        if event.key == pygame.K_RIGHT :
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT :
            self.ship.moving_left = False
        elif event.key == pygame.K_q :
            sys.exit()

    def fire_bullet(self) :
        """Creates a bullet and adds it to the bullet group"""
        #limiting the number of bullets you can fire
        if len(self.bullets) < self.settings.bullets_allowed :
            new_bullet = Bullet(self) 
            self.bullets.add(new_bullet)

    def update_bullets(self) :
        """This function updates the bullets and gets rid of ones that have passed out of screen"""
        #updating the bullets
        self.bullets.update()

        #deleting old bullets
        for bullet in self.bullets.copy() :
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)

    def create_fleet(self) :
        """This creates a fleet of aliens"""
        #Make an alien
        alien = Alien(self)
        self.aliens.add(alien)

    def update_screen(self) :
        """This function updates images and flips to the new screen"""
        #redraws the screen
        self.screen.fill(self.settings.bg_color) 
        #redraws the ship every time too
        self.ship.blitme()

        #drawing the bullets
        for bullet in self.bullets.sprites() :
            bullet.draw_bullet()

        #drawing aliens 
        self.aliens.draw(self.screen)

        pygame.display.flip()



if __name__ == '__main__' :

    ai = AlienInvasion()
    ai.run_game()

