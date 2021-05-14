#This is Alien Invasion which is based on the
#Alien invasion project in Python Crash Course
#Author is Alex Carpenter
#CPSC 223P 
#May 5th, 2021

#Big boy libraries
import sys 
from time import sleep
import pygame
#My libraries B)
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

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

        #creating game stats 
        self.stats = GameStats(self)

        #screen name
        pygame.display.set_caption("Alien Invasion") 

    def run_game(self) :
        """Main loop that runs the game and draws the game to the screen"""

        while True :
            
            #checks for events
            self.check_events()
            
            #updates screen accordingly
            self.update_screen()

            if self.stats.game_active :
                #and update the ship
                self.ship.update()

                #updating the bullets and deleting old ones
                self.update_bullets()

                #updating the aliens
                self.update_aliens()

            pygame.display.flip()

    def check_events(self) :
        """This handles key presses and updates accordingly"""
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()

            #this controls key down presses supports a and d or arrow keys
            elif event.type == pygame.KEYDOWN :
                self.check_keydown_events(event)

            #this controls key release events
            elif event.type == pygame.KEYUP :
                self.check_keyup_events(event)

            #this function handles mouse clicks since that requires a different check
            elif event.type == pygame.MOUSEBUTTONDOWN :
                self.check_mouse_down()

    
    def check_keydown_events(self, event) :
        """This function handles key down presses"""
        #have to check if the others are being held so you can't go double speed
        if event.key == pygame.K_d and self.ship.moving_right == False :
            #this moves the ship to the right
            self.ship.moving_d = True
        elif event.key == pygame.K_a and self.ship.moving_left == False :
            #this moves the ship to the left
            self.ship.moving_a = True
        elif event.key == pygame.K_RIGHT and self.ship.moving_d == False :
            #this moves the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT and self.ship.moving_a == False :
            #this moves the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE :
            #this handles firing the bullets
            self.fire_bullet()

    def check_mouse_down(self) :
        """As you can imagine by the name, this function only serves as a way to 
           check and fire bullets when the first mouse button is down"""
        if pygame.mouse.get_pressed()[0] :
            self.fire_bullet()

    def check_keyup_events(self, event) :
        """This function handles key release events"""
        if event.key == pygame.K_d :
            self.ship.moving_d = False
        elif event.key == pygame.K_a :
            self.ship.moving_a = False
        elif event.key == pygame.K_LEFT :
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT :
            self.ship.moving_right = False
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

        #Checking for bullet and alien collisions get destroyed aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens :
            #Destroy the existing bullets and create a new fleet. 
            self.bullets.empty()
            self.create_fleet()

    def create_fleet(self) :
        """This creates a fleet of aliens"""
        #Make an alien
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width) 
        number_aliens_x = available_space_x // (2 * alien_width)

        #determining number of rows of aliens we can have
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height) 

        #creating a row of aliens
        for row_number in range(number_rows) :
            for alien_number in range(number_aliens_x) :
                #Creating aliens and placing in row until out of space
                self.create_alien(alien_number, row_number)

    #of course we want to refactor the alien function to make it cleaner....
    def create_alien(self, alien_number, row_number) :
        """Helper function that creates aliens in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def check_fleet_edges(self) :
        """Changes the direction of the fleet if one hits an edge"""
        for alien in self.aliens.sprites() :
            if alien.check_edges() :
                self.change_fleet_direction()
                break

    def change_fleet_direction(self) :
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites() :
            alien.rect.y += self.settings.fleet_drop_speed 
        self.settings.fleet_direction *= -1

    def update_aliens(self) :
        """Calls the update function for aliens"""
        self.check_fleet_edges()
        self.aliens.update()

        #find ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens) :
            self.ship_hit()
            
        #checking if aliens reached the bottom 
        self.check_aliens_bottom()

    def ship_hit(self) :
        """Responding to ship being hit, evasive action!!!"""

        if self.stats.ships_left > 0 :
            #Lose a ship life, this is so sad
            self.stats.ships_left -= 1

            #Get rid of aliens and bullets we're resetting the level
            self.aliens.empty()
            self.bullets.empty()

            #Then recreate a fleet and center the ship
            self.create_fleet()
            self.ship.center_ship()

            #Pause game to let player grieve at their mistake
            sleep(1)
        else :
            self.stats.game_active = False

    #gotta say could've thought of a better function name hahahaa
    def check_aliens_bottom(self) :
        """Check if any aliens have reached the bottom, try not to laugh at the function name"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites() :
            if alien.rect.bottom >= screen_rect.bottom :
                #Treat this the same as if the ship got hit.
                self.ship_hit()
                break

    #I want the last function to be the update to the screen
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

